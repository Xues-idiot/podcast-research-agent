"""YouTube播客来源"""

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


class YouTubeSource(BaseSource):
    """YouTube播客来源处理器"""

    @property
    def source_type(self) -> SourceType:
        return SourceType.YOUTUBE

    def detect_source(self, url: str) -> bool:
        """检测URL是否为YouTube链接"""
        url_lower = url.lower()
        return "youtube.com" in url_lower or "youtu.be" in url_lower

    async def get_channel(self, url: str) -> PodcastChannel:
        """获取YouTube频道信息

        对于YouTube，支持：
        - 频道URL (youtube.com/@xxx, youtube.com/channel/xxx)
        - 播放列表URL
        - 视频URL (作为单集处理)
        """
        # 如果是视频URL，构建虚拟频道
        if "/watch" in url:
            return await self._channel_from_video(url)

        # 频道/播放列表
        info = await self._get_info(url)

        if "playlist" in url or info.get("entries"):
            # 播放列表
            return self._channel_from_playlist(info, url)
        else:
            # 频道
            return self._channel_from_channel(info, url)

    async def _get_info(self, url: str) -> dict:
        """获取页面信息"""
        ydl_opts = {
            "skip_download": True,
            "extract_flat": False,
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

    def _channel_from_video(self, url: str) -> PodcastChannel:
        """从视频URL构建虚拟频道"""
        info = self._get_info_sync(url, {"skip_download": True})
        video_id = info.get("id", "")

        episode = PodcastEpisode(
            source=SourceType.YOUTUBE,
            source_id=video_id,
            title=info.get("title", ""),
            description=info.get("description", ""),
            audio_url=self._get_audio_url_from_info(info),
            thumbnail_url=info.get("thumbnail"),
            duration=info.get("duration"),
            published_at=info.get("upload_date"),
            metadata={
                "channel_id": info.get("channel_id"),
                "channel_title": info.get("channel"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
            }
        )

        return PodcastChannel(
            source=SourceType.YOUTUBE,
            source_id=info.get("channel_id", video_id),
            title=info.get("channel", "YouTube"),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=[episode],
            metadata={
                "channel_id": info.get("channel_id"),
                "uploader": info.get("uploader"),
            }
        )

    def _channel_from_channel(self, info: dict, url: str) -> PodcastChannel:
        """从频道信息构建频道对象"""
        channel_id = info.get("id", "")

        episodes = []
        if "entries" in info:
            for entry in info["entries"]:
                if entry:
                    episodes.append(PodcastEpisode(
                        source=SourceType.YOUTUBE,
                        source_id=entry.get("id", ""),
                        title=entry.get("title", ""),
                        description=entry.get("description", ""),
                        audio_url=self._get_audio_url_from_info(entry),
                        thumbnail_url=entry.get("thumbnail"),
                        duration=entry.get("duration"),
                        published_at=entry.get("upload_date"),
                        metadata={
                            "channel_title": entry.get("channel"),
                        }
                    ))

        return PodcastChannel(
            source=SourceType.YOUTUBE,
            source_id=channel_id,
            title=info.get("title", info.get("channel", "YouTube Channel")),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=episodes,
            metadata={
                "subscribers": info.get("subscriber_count"),
                "uploader": info.get("uploader"),
            }
        )

    def _channel_from_playlist(self, info: dict, url: str) -> PodcastChannel:
        """从播放列表构建频道对象"""
        playlist_id = info.get("id", "")

        episodes = []
        if "entries" in info:
            for entry in info["entries"]:
                if entry:
                    episodes.append(PodcastEpisode(
                        source=SourceType.YOUTUBE,
                        source_id=entry.get("id", ""),
                        title=entry.get("title", ""),
                        description=entry.get("description", ""),
                        audio_url=self._get_audio_url_from_info(entry),
                        thumbnail_url=entry.get("thumbnail"),
                        duration=entry.get("duration"),
                        published_at=entry.get("upload_date"),
                        metadata={
                            "channel_title": entry.get("channel"),
                        }
                    ))

        return PodcastChannel(
            source=SourceType.YOUTUBE,
            source_id=playlist_id,
            title=info.get("title", "YouTube Playlist"),
            description=info.get("description", ""),
            feed_url=url,
            thumbnail_url=info.get("thumbnail"),
            episodes=episodes,
            metadata={
                "playlist_type": "youtube_playlist",
                "uploader": info.get("uploader"),
            }
        )

    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取YouTube单集信息"""
        info = await self._get_info(url)
        video_id = info.get("id", "")

        return PodcastEpisode(
            source=SourceType.YOUTUBE,
            source_id=video_id,
            title=info.get("title", ""),
            description=info.get("description", ""),
            audio_url=self._get_audio_url_from_info(info),
            thumbnail_url=info.get("thumbnail"),
            duration=info.get("duration"),
            published_at=info.get("upload_date"),
            metadata={
                "channel_id": info.get("channel_id"),
                "channel_title": info.get("channel"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
            }
        )

    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取YouTube音频URL"""
        if episode.audio_url:
            return episode.audio_url

        # 重新获取
        info = await self._get_info(
            f"https://www.youtube.com/watch?v={episode.source_id}"
        )
        return self._get_audio_url_from_info(info)

    def _get_audio_url_from_info(self, info: dict) -> str:
        """从视频信息中提取音频URL"""
        # 优先获取音频直链
        if "requested_formats" in info:
            for fmt in info["requested_formats"]:
                if fmt.get("ext") in ("mp3", "m4a", "webm"):
                    return fmt.get("url", "")

        if "formats" in info:
            for fmt in info["formats"]:
                if fmt.get("ext") in ("mp3", "m4a", "webm") and fmt.get("url"):
                    return fmt.get("url", "")

        # 返回无格式信息时的占位
        video_id = info.get("id", "")
        return f"https://www.youtube.com/watch?v={video_id}"


# 全局单例
_youtube_source: Optional[YouTubeSource] = None


def get_youtube_source() -> YouTubeSource:
    """获取YouTube来源单例"""
    global _youtube_source
    if _youtube_source is None:
        _youtube_source = YouTubeSource()
    return _youtube_source
