"""Bilibili播客来源"""

import asyncio
import re
from typing import Optional

import yt_dlp

from echo.sources import (
    BaseSource,
    PodcastChannel,
    PodcastEpisode,
    SourceType,
)


class BilibiliSource(BaseSource):
    """Bilibili播客来源处理器"""

    @property
    def source_type(self) -> SourceType:
        return SourceType.BILIBILI

    def detect_source(self, url: str) -> bool:
        """检测URL是否为B站链接"""
        url_lower = url.lower()
        return "bilibili.com" in url_lower or "b23.tv" in url_lower

    async def get_channel(self, url: str) -> PodcastChannel:
        """获取B站频道信息

        支持:
        - 视频页 (bilibili.com/video/BVxxx)
        - 频道页 (bilibili.com/channel/xxx)
        - 播放列表 (bilibili.complaylist/xxx)
        - 短链接 (b23.tv/xxx)
        """
        # 先解析短链接
        url = await self._resolve_short_url(url)

        # 判断URL类型
        if "/video/" in url:
            return await self._channel_from_video(url)
        elif "/channel/" in url or "/space/" in url:
            return await self._channel_from_user(url)
        elif "/playlist/" in url:
            return await self._channel_from_playlist(url)
        else:
            # 默认当视频处理
            return await self._channel_from_video(url)

    async def _resolve_short_url(self, url: str) -> str:
        """解析B站短链接"""
        if "b23.tv" not in url.lower():
            return url

        try:
            import httpx
            async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
                response = await client.head(url)
                return str(response.url)
        except Exception:
            return url

    async def _get_info(self, url: str) -> dict:
        """获取页面信息"""
        ydl_opts = {
            "skip_download": True,
            "extractor_args": {
                "bilibili": {
                    "cookie": "cookies.txt",  # 可选，需要登录
                }
            },
        }
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self._get_info_sync(url, ydl_opts)
        )

    def _get_info_sync(self, url: str, ydl_opts: dict) -> dict:
        """同步获取信息"""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    async def _channel_from_video(self, url: str) -> PodcastChannel:
        """从视频URL构建虚拟频道"""
        info = await self._get_info(url)
        bvid = info.get("id", "")

        episode = PodcastEpisode(
            source=SourceType.BILIBILI,
            source_id=bvid,
            title=info.get("title", ""),
            description=info.get("description", ""),
            audio_url=self._get_audio_url_from_info(info),
            thumbnail_url=info.get("thumbnail"),
            duration=info.get("duration"),
            published_at=info.get("upload_date"),
            metadata={
                "aid": info.get("display_id"),
                "bvid": bvid,
                "owner": info.get("uploader"),
                "owner_mid": info.get("channel_id"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
                "coin_count": info.get("coin_count"),
                "favorite_count": info.get("favorite_count"),
                "share_count": info.get("share_count"),
                "danmaku": info.get("no_sponsored_descriptors"),
            }
        )

        return PodcastChannel(
            source=SourceType.BILIBILI,
            source_id=bvid,
            title=info.get("uploader", info.get("channel", "Bilibili")),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=[episode],
            metadata={
                "mid": info.get("channel_id"),
                "uploader": info.get("uploader"),
            }
        )

    async def _channel_from_user(self, url: str) -> PodcastChannel:
        """从用户空间构建频道"""
        info = await self._get_info(url)

        channel_id = info.get("channel_id", info.get("id", ""))

        episodes = []
        if "entries" in info:
            for entry in info["entries"]:
                if entry:
                    episodes.append(PodcastEpisode(
                        source=SourceType.BILIBILI,
                        source_id=entry.get("id", ""),
                        title=entry.get("title", ""),
                        description=entry.get("description", ""),
                        audio_url=self._get_audio_url_from_info(entry),
                        thumbnail_url=entry.get("thumbnail"),
                        duration=entry.get("duration"),
                        published_at=entry.get("upload_date"),
                        metadata={
                            "aid": entry.get("display_id"),
                            "owner": entry.get("uploader"),
                        }
                    ))

        return PodcastChannel(
            source=SourceType.BILIBILI,
            source_id=str(channel_id),
            title=info.get("uploader", info.get("title", "Bilibili User")),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=episodes,
            metadata={
                "type": "user_channel",
                "uploader": info.get("uploader"),
            }
        )

    async def _channel_from_playlist(self, url: str) -> PodcastChannel:
        """从播放列表构建频道"""
        info = await self._get_info(url)

        playlist_id = info.get("id", "")

        episodes = []
        if "entries" in info:
            for entry in info["entries"]:
                if entry:
                    episodes.append(PodcastEpisode(
                        source=SourceType.BILIBILI,
                        source_id=entry.get("id", ""),
                        title=entry.get("title", ""),
                        description=entry.get("description", ""),
                        audio_url=self._get_audio_url_from_info(entry),
                        thumbnail_url=entry.get("thumbnail"),
                        duration=entry.get("duration"),
                        published_at=entry.get("upload_date"),
                        metadata={
                            "aid": entry.get("display_id"),
                            "owner": entry.get("uploader"),
                        }
                    ))

        return PodcastChannel(
            source=SourceType.BILIBILI,
            source_id=playlist_id,
            title=info.get("title", "Bilibili Playlist"),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=episodes,
            metadata={
                "type": "playlist",
                "uploader": info.get("uploader"),
            }
        )

    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取B站单集信息"""
        url = await self._resolve_short_url(url)
        info = await self._get_info(url)
        bvid = info.get("id", "")

        return PodcastEpisode(
            source=SourceType.BILIBILI,
            source_id=bvid,
            title=info.get("title", ""),
            description=info.get("description", ""),
            audio_url=self._get_audio_url_from_info(info),
            thumbnail_url=info.get("thumbnail"),
            duration=info.get("duration"),
            published_at=info.get("upload_date"),
            metadata={
                "aid": info.get("display_id"),
                "bvid": bvid,
                "owner": info.get("uploader"),
                "owner_mid": info.get("channel_id"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
            }
        )

    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取B站音频URL"""
        if episode.audio_url:
            return episode.audio_url

        # 重新获取
        bvid = episode.source_id
        url = f"https://www.bilibili.com/video/{bvid}"
        info = await self._get_info(url)
        return self._get_audio_url_from_info(info)

    def _get_audio_url_from_info(self, info: dict) -> str:
        """从视频信息中提取音频URL"""
        # B站没有直接的音频流，返回视频直链供下载器处理
        if "requested_formats" in info:
            for fmt in info["requested_formats"]:
                if fmt.get("ext") in ("mp3", "m4a", "webm"):
                    return fmt.get("url", "")

        if "formats" in info:
            for fmt in info["formats"]:
                if fmt.get("ext") in ("mp3", "m4a", "webm") and fmt.get("url"):
                    return fmt.get("url", "")

        # 返回无格式信息时的占位
        bvid = info.get("id", "")
        return f"https://www.bilibili.com/video/{bvid}"


# 全局单例
_bilibili_source: Optional[BilibiliSource] = None


def get_bilibili_source() -> BilibiliSource:
    """获取Bilibili来源单例"""
    global _bilibili_source
    if _bilibili_source is None:
        _bilibili_source = BilibiliSource()
    return _bilibili_source
