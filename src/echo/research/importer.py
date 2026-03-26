"""播客导入器 - 从外部平台导入播客内容"""

import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional
import httpx


@dataclass
class ImportedPodcast:
    """导入的播客"""
    id: str = ""
    title: str = ""
    description: str = ""
    feed_url: str = ""
    source_url: str = ""
    platform: str = ""
    image_url: str = ""
    author: str = ""
    episodes: list = field(default_factory=list)
    imported_at: str = ""

    def __post_init__(self):
        if not self.imported_at:
            self.imported_at = datetime.now().isoformat()


@dataclass
class ImportedEpisode:
    """导入的剧集"""
    id: str = ""
    title: str = ""
    description: str = ""
    audio_url: str = ""
    duration: int = 0
    published_at: str = ""
    image_url: str = ""


class PodcastImporter:
    """播客导入器"""

    # 支持的平台
    SUPPORTED_PLATFORMS = {
        "apple": r"podcasts\.apple\.com",
        "spotify": r"open\.spotify\.com",
        "google": r"podcasts\.google\.com",
        "overcast": r"overcast\.fm",
        "pocketcasts": r"pocketcasts\.com",
        "castbox": r"castbox\.fm",
        "breaker": r"breaker\.com",
        "radiopublic": r"radiopublic\.com",
    }

    def __init__(self, storage_path: Optional[str] = None):
        """初始化导入器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "imports"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._imports_file = self.storage_path / "imports.json"
        self._imports: dict[str, ImportedPodcast] = {}
        self._load()

    def _load(self):
        """加载导入数据"""
        if self._imports_file.exists():
            try:
                with open(self._imports_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for imp_data in data.values():
                        self._imports[imp_data["id"]] = ImportedPodcast(**imp_data)
            except (json.JSONDecodeError, KeyError):
                self._imports = {}

    def _save(self):
        """保存导入数据"""
        data = {pid: imp.__dict__ for pid, imp in self._imports.items()}
        temp_file = self._imports_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._imports_file)

    def detect_platform(self, url: str) -> Optional[str]:
        """检测URL对应的平台

        Args:
            url: 播客URL

        Returns:
            平台名称
        """
        for platform, pattern in self.SUPPORTED_PLATFORMS.items():
            if re.search(pattern, url, re.IGNORECASE):
                return platform
        return None

    async def import_from_url(self, url: str) -> ImportedPodcast:
        """从URL导入播客

        Args:
            url: 播客或RSS URL

        Returns:
            导入的播客
        """
        # 检测平台
        platform = self.detect_platform(url)

        # 如果是RSS URL，直接解析
        if "rss" in url.lower() or "feed" in url.lower():
            return await self._import_rss(url)

        # 否则尝试检测并跳转
        if platform == "apple":
            return await self._import_apple_podcast(url)
        elif platform == "spotify":
            return await self._import_spotify_podcast(url)

        # 默认尝试作为RSS解析
        return await self._import_rss(url)

    async def _import_rss(self, feed_url: str) -> ImportedPodcast:
        """导入RSS源

        Args:
            feed_url: RSS Feed URL

        Returns:
            导入的播客
        """
        podcast = ImportedPodcast(
            feed_url=feed_url,
            platform="rss",
        )

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(feed_url)
                response.raise_for_status()
                content = response.text

            # 简单解析RSS
            podcast.title = self._extract_rss_field(content, "title")
            podcast.description = self._extract_rss_field(content, "description")
            podcast.image_url = self._extract_rss_field(content, "image")
            podcast.author = self._extract_rss_field(content, "author")

            # 提取剧集
            episodes = self._extract_rss_episodes(content)
            podcast.episodes = [
                {
                    "id": ep.get("guid", f"ep_{i}"),
                    "title": ep.get("title", ""),
                    "description": ep.get("description", ""),
                    "audio_url": ep.get("audio_url", ""),
                    "duration": self._parse_duration(ep.get("duration", "")),
                    "published_at": ep.get("pubDate", ""),
                }
                for i, ep in enumerate(episodes[:50])  # 最多50集
            ]

        except Exception as e:
            podcast.description = f"导入失败: {str(e)}"

        self._imports[podcast.id] = podcast
        self._save()
        return podcast

    def _extract_rss_field(self, content: str, field: str) -> str:
        """提取RSS字段"""
        patterns = {
            "title": r"<title><!\[CDATA\[([^\]]+)\]\]></title>|<title>([^<]+)</title>",
            "description": r"<description><!\[CDATA\[([^\]]+)\]\]></description>|<description>([^<]+)</description>",
            "image": r"<image><url><!\[CDATA\[([^\]]+)\]\]></url>|<image><url>([^<]+)</url>",
            "author": r"<author><!\[CDATA\[([^\]]+)\]\]></author>|<author>([^<]+)</author>",
        }

        pattern = patterns.get(field, "")
        if not pattern:
            return ""

        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1) or match.group(2) or ""
        return ""

    def _extract_rss_episodes(self, content: str) -> list[dict]:
        """提取RSS剧集列表"""
        episodes = []

        # 查找所有item
        item_pattern = r"<item>(.*?)</item>"
        items = re.findall(item_pattern, content, re.DOTALL | re.IGNORECASE)

        for item in items:
            episode = {}

            # 提取标题
            title_match = re.search(r"<title><!\[CDATA\[([^\]]+)\]\]></title>|<title>([^<]+)</title>", item, re.IGNORECASE)
            if title_match:
                episode["title"] = title_match.group(1) or title_match.group(2) or ""

            # 提取描述
            desc_match = re.search(r"<description><!\[CDATA\[([^\]]+)\]\]></description>|<description>([^<]+)</description>", item, re.IGNORECASE)
            if desc_match:
                episode["description"] = desc_match.group(1) or desc_match.group(2) or ""

            # 提取音频URL
            audio_match = re.search(r"<enclosure[^>]+url=[\"']([^\"']+)[\"']", item, re.IGNORECASE)
            if audio_match:
                episode["audio_url"] = audio_match.group(1)

            # 提取时长
            duration_match = re.search(r"<itunes:duration>([^<]+)</itunes:duration>", item, re.IGNORECASE)
            if duration_match:
                episode["duration"] = duration_match.group(1)

            # 提取发布日期
            pub_match = re.search(r"<pubDate>([^<]+)</pubDate>", item, re.IGNORECASE)
            if pub_match:
                episode["pubDate"] = pub_match.group(1)

            # 提取GUID
            guid_match = re.search(r"<guid[^>]*>([^<]+)</guid>", item, re.IGNORECASE)
            if guid_match:
                episode["guid"] = guid_match.group(1)

            if episode.get("audio_url"):
                episodes.append(episode)

        return episodes

    def _parse_duration(self, duration_str: str) -> int:
        """解析时长字符串为秒数"""
        if not duration_str:
            return 0

        try:
            # HH:MM:SS 或 MM:SS 格式
            parts = duration_str.split(":")
            if len(parts) == 3:
                return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            elif len(parts) == 2:
                return int(parts[0]) * 60 + int(parts[1])
            else:
                return int(duration_str)
        except:
            return 0

    async def _import_apple_podcast(self, url: str) -> ImportedPodcast:
        """导入Apple Podcast"""
        # Apple Podcasts需要通过RSS Feed导入，这里简化处理
        podcast = ImportedPodcast(
            source_url=url,
            platform="apple",
            description="Apple Podcasts 需要使用RSS Feed导入",
        )
        self._imports[podcast.id] = podcast
        self._save()
        return podcast

    async def _import_spotify_podcast(self, url: str) -> ImportedPodcast:
        """导入Spotify Podcast"""
        podcast = ImportedPodcast(
            source_url=url,
            platform="spotify",
            description="Spotify Podcast 需要使用RSS Feed导入",
        )
        self._imports[podcast.id] = podcast
        self._save()
        return podcast

    def get_imports(self) -> list[ImportedPodcast]:
        """获取所有导入记录"""
        return sorted(
            self._imports.values(),
            key=lambda x: x.imported_at,
            reverse=True
        )

    def get_import(self, import_id: str) -> Optional[ImportedPodcast]:
        """获取导入记录"""
        return self._imports.get(import_id)

    def delete_import(self, import_id: str) -> bool:
        """删除导入记录"""
        if import_id in self._imports:
            del self._imports[import_id]
            self._save()
            return True
        return False


# 全局实例
_podcast_importer: Optional[PodcastImporter] = None


def get_podcast_importer() -> PodcastImporter:
    """获取全局导入器"""
    global _podcast_importer
    if _podcast_importer is None:
        _podcast_importer = PodcastImporter()
    return _podcast_importer
