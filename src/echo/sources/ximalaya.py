"""喜马拉雅播客来源"""

import asyncio
import hashlib
import re
from typing import Optional

import httpx

from echo.sources import (
    BaseSource,
    PodcastChannel,
    PodcastEpisode,
    SourceType,
)


class XimalayaSource(BaseSource):
    """喜马拉雅播客来源处理器

    喜马拉雅 (ximalaya.com) 是国内知名播客平台
    """

    BASE_URL = "https://www.ximalaya.com"

    @property
    def source_type(self) -> SourceType:
        return SourceType.XIMALAYA

    def detect_source(self, url: str) -> bool:
        """检测URL是否为喜马拉雅链接"""
        url_lower = url.lower()
        return "ximalaya" in url_lower or "喜马拉雅" in url

    async def get_channel(self, url: str) -> PodcastChannel:
        """获取喜马拉雅频道信息"""
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)
            response.raise_for_status()
            html = response.text

            # 提取播客信息
            channel_info = self._parse_channel_page(html, url)

            # 获取节目列表
            episodes = await self._get_episodes(
                client,
                channel_info["album_id"],
                channel_info["category"]
            )

            return PodcastChannel(
                source=SourceType.XIMALAYA,
                source_id=str(channel_info["album_id"]),
                title=channel_info["title"],
                description=channel_info["description"],
                feed_url=url,
                thumbnail_url=channel_info.get("thumbnail"),
                episodes=episodes,
                metadata=channel_info.get("metadata", {})
            )

    def _parse_channel_page(self, html: str, url: str) -> dict:
        """解析频道页面"""
        import json

        # 尝试查找JSON数据
        state_match = re.search(
            r'window\.__INITIAL_STATE__\s*=\s*({.*?})\s*;',
            html,
            re.DOTALL
        )

        album_id = self._extract_album_id_from_url(url)
        category = self._extract_category_from_url(url)

        if state_match:
            try:
                state = json.loads(state_match.group(1))
                album_data = state.get("album", {}).get("albumInfo", {})

                if album_data:
                    return {
                        "album_id": album_data.get("albumId", album_id),
                        "title": album_data.get("albumTitle", ""),
                        "description": album_data.get("intro", ""),
                        "thumbnail": album_data.get("cover"),
                        "category": category,
                        "metadata": {
                            "anchor_id": album_data.get("anchorId"),
                            "anchor_name": album_data.get("anchorName"),
                            "track_count": album_data.get("trackCount"),
                        }
                    }
            except json.JSONDecodeError:
                pass

        # 尝试从meta标签提取
        title_match = re.search(
            r'<meta[^>]*property="og:title"[^>]*content="([^"]*)"',
            html
        )
        desc_match = re.search(
            r'<meta[^>]*name="description"[^>]*content="([^"]*)"',
            html
        )
        image_match = re.search(
            r'<meta[^>]*property="og:image"[^>]*content="([^"]*)"',
            html
        )

        return {
            "album_id": album_id,
            "title": title_match.group(1) if title_match else "喜马拉雅播客",
            "description": desc_match.group(1) if desc_match else "",
            "thumbnail": image_match.group(1) if image_match else None,
            "category": category,
            "metadata": {}
        }

    def _extract_album_id_from_url(self, url: str) -> str:
        """从URL提取专辑ID"""
        # URL格式: https://www.ximalaya.com/{category}/{album_id}/
        match = re.search(r'/(\d+)/?$', url)
        if match:
            return match.group(1)

        # 尝试更多模式
        match = re.search(r'/(\d+)/re albums', url)
        if match:
            return match.group(1)

        return hashlib.md5(url.encode()).hexdigest()[:8]

    def _extract_category_from_url(self, url: str) -> str:
        """从URL提取分类"""
        # URL格式: https://www.ximalaya.com/{category}/{album_id}/
        match = re.search(r'ximalaya\.com/([^/]+)/', url)
        if match:
            return match.group(1)
        return "audio"

    async def _get_episodes(
        self,
        client: httpx.AsyncClient,
        album_id: str,
        category: str
    ) -> list:
        """获取专辑节目列表"""
        # 喜马拉雅API
        api_url = f"{self.BASE_URL}//{category}/{album_id}"

        try:
            # 尝试获取第一页
            response = await client.get(
                f"{self.BASE_URL}/revision/{category}/album/{album_id}",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                }
            )

            if response.status_code == 200:
                data = response.json()
                return self._parse_episodes_from_api(data)
        except Exception:
            pass

        return []

    def _parse_episodes_from_api(self, data: dict) -> list:
        """从API响应解析节目列表"""
        episodes = []

        main_info = data.get("data", {}).get("mainInfo", {})
        tracks = main_info.get("tracks", [])

        for track in tracks:
            episode = PodcastEpisode(
                source=SourceType.XIMALAYA,
                source_id=str(track.get("trackId", "")),
                title=track.get("title", ""),
                description=track.get("intro", ""),
                audio_url=track.get("playUrl64", ""),
                thumbnail_url=track.get("cover"),
                duration=track.get("duration"),
                published_at=track.get("createdAt"),
                metadata={
                    "like_count": track.get("likeCount"),
                    "play_count": track.get("playCount"),
                    "comment_count": track.get("commentCount"),
                    "share_count": track.get("shareCount"),
                }
            )
            episodes.append(episode)

        return episodes

    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取喜马拉雅单集信息"""
        album_id = self._extract_album_id_from_url(url)
        category = self._extract_category_from_url(url)

        async with httpx.AsyncClient(timeout=30) as client:
            try:
                response = await client.get(
                    f"{self.BASE_URL}/revision/track/getTrackDetailInfo",
                    params={
                        "trackId": album_id,
                        "albumId": album_id,
                    },
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    }
                )

                if response.status_code == 200:
                    data = response.json()
                    track = data.get("data", {})
                    return PodcastEpisode(
                        source=SourceType.XIMALAYA,
                        source_id=str(track.get("trackId", album_id)),
                        title=track.get("title", ""),
                        description=track.get("intro", ""),
                        audio_url=track.get("playUrl64", ""),
                        thumbnail_url=track.get("cover"),
                        duration=track.get("duration"),
                        published_at=track.get("createdAt"),
                        metadata={
                            "album_id": track.get("albumId"),
                            "album_title": track.get("albumTitle"),
                        }
                    )
            except Exception:
                pass

        # 占位实现
        return PodcastEpisode(
            source=SourceType.XIMALAYA,
            source_id=album_id,
            title="喜马拉雅播客单集",
            description="",
            audio_url="",
        )

    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取喜马拉雅音频URL"""
        if episode.audio_url:
            return episode.audio_url

        # 尝试重新获取
        ep = await self.get_episode(
            f"{self.BASE_URL}/audio/{episode.source_id}"
        )
        return ep.audio_url


# 全局单例
_ximalaya_source: Optional[XimalayaSource] = None


def get_ximalaya_source() -> XimalayaSource:
    """获取喜马拉雅来源单例"""
    global _ximalaya_source
    if _ximalaya_source is None:
        _ximalaya_source = XimalayaSource()
    return _ximalaya_source
