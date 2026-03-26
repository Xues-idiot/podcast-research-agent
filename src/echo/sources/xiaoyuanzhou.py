"""小宇宙播客来源"""

import asyncio
import hashlib
import json
import re
from typing import Optional

import httpx

from echo.sources import (
    BaseSource,
    PodcastChannel,
    PodcastEpisode,
    SourceType,
)


class XiaoyuanzhouSource(BaseSource):
    """小宇宙播客来源处理器

    小宇宙 (xiaoyuanzhou.com, xyz) 是国内播客平台
    """

    BASE_URL = "https://www.xiaoyuanzhou.com"

    @property
    def source_type(self) -> SourceType:
        return SourceType.XIAOYUANZHOU

    def detect_source(self, url: str) -> bool:
        """检测URL是否为小宇宙链接"""
        url_lower = url.lower()
        return "xiaoyuanzhou" in url_lower or "xyz" in url_lower

    async def get_channel(self, url: str) -> PodcastChannel:
        """获取小宇宙频道信息"""
        async with httpx.AsyncClient(timeout=30) as client:
            # 获取页面内容
            response = await client.get(url)
            response.raise_for_status()
            html = response.text

            # 提取播客信息
            channel_info = await self._parse_channel_page(html, url)

            # 获取节目列表
            episodes = await self._get_episodes(client, channel_info["id"])

            return PodcastChannel(
                source=SourceType.XIAOYUANZHOU,
                source_id=channel_info["id"],
                title=channel_info["title"],
                description=channel_info["description"],
                feed_url=url,
                thumbnail_url=channel_info.get("thumbnail"),
                episodes=episodes,
                metadata=channel_info.get("metadata", {})
            )

    async def _parse_channel_page(self, html: str, url: str) -> dict:
        """解析频道页面"""
        # 尝试从HTML中提取JSON数据

        # 查找window.__INITIAL_STATE__或类似的数据
        state_match = re.search(
            r'window\.__INITIAL_STATE__\s*=\s*({.*?})\s*;',
            html,
            re.DOTALL
        )

        if state_match:
            try:
                state = json.loads(state_match.group(1))
                # 从state中提取播客信息
                podcast = state.get("podcast", {})
                return {
                    "id": podcast.get("id", ""),
                    "title": podcast.get("title", ""),
                    "description": podcast.get("description", ""),
                    "thumbnail": podcast.get("coverUrl"),
                    "metadata": {
                        "rss": podcast.get("rss"),
                        "author": podcast.get("author"),
                    }
                }
            except json.JSONDecodeError:
                pass

        # 尝试从meta标签提取
        title_match = re.search(r'<meta[^>]*property="og:title"[^>]*content="([^"]*)"', html)
        desc_match = re.search(r'<meta[^>]*property="og:description"[^>]*content="([^"]*)"', html)
        image_match = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]*)"', html)

        # 从URL提取ID
        url_id = self._extract_id_from_url(url)

        return {
            "id": url_id,
            "title": title_match.group(1) if title_match else "小宇宙播客",
            "description": desc_match.group(1) if desc_match else "",
            "thumbnail": image_match.group(1) if image_match else None,
            "metadata": {}
        }

    def _extract_id_from_url(self, url: str) -> str:
        """从URL提取播客ID"""
        # URL格式: https://www.xiaoyuanzhou.com/podcasts/xxx
        match = re.search(r'/podcasts/([^/?]+)', url)
        if match:
            return match.group(1)
        return hashlib.md5(url.encode()).hexdigest()[:8]

    async def _get_episodes(self, client: httpx.AsyncClient, podcast_id: str) -> list:
        """获取播客节目列表"""
        # 尝试调用小宇宙API
        api_url = f"{self.BASE_URL}/api/v1/podcasts/{podcast_id}/episodes"

        try:
            response = await client.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return self._parse_episodes_from_api(data)
        except Exception:
            pass

        return []

    def _parse_episodes_from_api(self, data: dict) -> list:
        """从API响应解析节目列表"""
        episodes = []

        items = data.get("data", {}).get("items", [])
        for item in items:
            episode = PodcastEpisode(
                source=SourceType.XIAOYUANZHOU,
                source_id=str(item.get("id", "")),
                title=item.get("title", ""),
                description=item.get("description", ""),
                audio_url=item.get("audioUrl", ""),
                thumbnail_url=item.get("coverUrl"),
                duration=item.get("duration"),
                published_at=item.get("publishedAt"),
                metadata={
                    "play_count": item.get("playCount"),
                    "like_count": item.get("likeCount"),
                }
            )
            episodes.append(episode)

        return episodes

    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取小宇宙单集信息"""
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)
            response.raise_for_status()
            html = response.text

            return await self._parse_episode_page(html, url)

    async def _parse_episode_page(self, html: str, url: str) -> PodcastEpisode:
        """解析单集页面"""
        # 查找页面数据
        state_match = re.search(
            r'window\.__INITIAL_STATE__\s*=\s*({.*?})\s*;',
            html,
            re.DOTALL
        )

        if state_match:
            try:
                state = json.loads(state_match.group(1))
                episode_data = state.get("episode", {})
                podcast_data = state.get("podcast", {})

                return PodcastEpisode(
                    source=SourceType.XIAOYUANZHOU,
                    source_id=str(episode_data.get("id", "")),
                    title=episode_data.get("title", ""),
                    description=episode_data.get("description", ""),
                    audio_url=episode_data.get("audioUrl", ""),
                    thumbnail_url=episode_data.get("coverUrl"),
                    duration=episode_data.get("duration"),
                    published_at=episode_data.get("publishedAt"),
                    metadata={
                        "podcast_id": podcast_data.get("id"),
                        "podcast_title": podcast_data.get("title"),
                    }
                )
            except json.JSONDecodeError:
                pass

        # 占位实现
        return PodcastEpisode(
            source=SourceType.XIAOYUANZHOU,
            source_id=self._extract_id_from_url(url),
            title="小宇宙播客单集",
            description="",
            audio_url="",
        )

    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取小宇宙音频URL"""
        if episode.audio_url:
            return episode.audio_url

        # 尝试重新获取
        url = f"{self.BASE_URL}/episodes/{episode.source_id}"
        ep = await self.get_episode(url)
        return ep.audio_url


# 全局单例
_xiaoyuanzhou_source: Optional[XiaoyuanzhouSource] = None


def get_xiaoyuanzhou_source() -> XiaoyuanzhouSource:
    """获取小宇宙来源单例"""
    global _xiaoyuanzhou_source
    if _xiaoyuanzhou_source is None:
        _xiaoyuanzhou_source = XiaoyuanzhouSource()
    return _xiaoyuanzhou_source
