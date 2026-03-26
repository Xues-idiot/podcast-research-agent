"""RSS播客来源"""

import asyncio
import re
from datetime import datetime
from typing import List, Optional

import feedparser

from echo.sources import (
    BaseSource,
    PodcastChannel,
    PodcastEpisode,
    SourceType,
)


class RSSSource(BaseSource):
    """RSS播客来源处理器

    支持标准RSS 2.0和Atom格式的播客订阅源
    """

    @property
    def source_type(self) -> SourceType:
        return SourceType.RSS

    def detect_source(self, url: str) -> bool:
        """检测URL是否为RSS订阅源"""
        url_lower = url.lower()
        return (
            ".xml" in url_lower
            or ".rss" in url_lower
            or "feed" in url_lower
            or "rss" in url_lower
        )

    async def get_channel(self, url: str) -> PodcastChannel:
        """获取RSS频道信息"""
        feed = await asyncio.run_in_executor(
            None,
            lambda: feedparser.parse(url)
        )

        channel = feed.feed if feed.feed else {}

        episodes = []
        for entry in feed.entries:
            episode = self._parse_entry(entry)
            episodes.append(episode)

        return PodcastChannel(
            source=SourceType.RSS,
            source_id=self._get_feed_id(channel, url),
            title=channel.get("title", "RSS Feed"),
            description=channel.get("description", ""),
            feed_url=url,
            thumbnail_url=self._get_thumbnail(channel),
            episodes=episodes,
            metadata={
                "language": channel.get("language"),
                "link": channel.get("link"),
                "last_updated": channel.get("updated"),
            }
        )

    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取RSS单集信息（通过遍历频道）"""
        # RSS单集URL通常是条目的link
        feed = await asyncio.run_in_executor(
            None,
            lambda: feedparser.parse(url)
        )

        # 如果URL指向的是单个条目
        if feed.entries:
            return self._parse_entry(feed.entries[0])

        # 否则尝试解析整个频道并查找
        # 这是一个占位实现
        raise ValueError(f"Cannot find episode at URL: {url}")

    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取RSS音频URL"""
        return episode.audio_url

    def _parse_entry(self, entry) -> PodcastEpisode:
        """解析RSS条目为PodcastEpisode"""
        # 提取音频URL
        audio_url = ""
        if hasattr(entry, "enclosures") and entry.enclosures:
            audio_url = entry.enclosures[0].get("href", "")

        # 如果没有enclosures，尝试media
        if not audio_url:
            if hasattr(entry, "media_content") and entry.media_content:
                audio_url = entry.media_content[0].get("url", "")
            elif hasattr(entry, "links"):
                for link in entry.links:
                    if link.get("type", "").startswith("audio/"):
                        audio_url = link.get("href", "")
                        break

        # 解析发布时间
        published_at = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            try:
                dt = datetime(*entry.published_parsed[:6])
                published_at = dt.isoformat()
            except Exception:
                pass

        # 解析时长
        duration = None
        if hasattr(entry, "itunes_duration"):
            duration = self._parse_duration(entry.itunes_duration)

        # 提取缩略图
        thumbnail_url = None
        if hasattr(entry, "image") and entry.image:
            thumbnail_url = entry.image.get("href")

        return PodcastEpisode(
            source=SourceType.RSS,
            source_id=entry.get("id", entry.get("link", "")),
            title=entry.get("title", ""),
            description=entry.get("description", entry.get("summary", "")),
            audio_url=audio_url,
            thumbnail_url=thumbnail_url,
            duration=duration,
            published_at=published_at,
            metadata={
                "link": entry.get("link"),
                "author": entry.get("author"),
                "guid": entry.get("id"),
            }
        )

    def _get_feed_id(self, channel: dict, url: str) -> str:
        """获取订阅源ID"""
        # channel 是 feedparser 返回的 dict-like 对象
        channel_id = channel.get("id") or channel.get("uuid")
        if channel_id:
            return str(channel_id)
        # 使用URL作为后备ID
        return url

    def _get_thumbnail(self, channel: dict) -> Optional[str]:
        """获取频道缩略图"""
        # 优先从itunes获取
        if hasattr(channel, "itunes_image") and channel.itunes_image:
            return channel.itunes_image.get("href")

        # 从image获取
        if hasattr(channel, "image") and channel.image:
            if isinstance(channel.image, dict):
                return channel.image.get("href")
            return str(channel.image)

        return None

    def _parse_duration(self, duration_str) -> Optional[int]:
        """解析时长字符串为秒数

        支持格式:
        - 3600 (秒)
        - 1:00:00 (时:分:秒)
        - 60:00 (分:秒)
        - "1 hour" (自然语言)
        """
        if not duration_str:
            return None

        # 如果是数字字符串
        if isinstance(duration_str, (int, float)):
            return int(duration_str)

        duration_str = str(duration_str)

        # 尝试 HH:MM:SS 格式
        if ":" in duration_str:
            parts = duration_str.split(":")
            if len(parts) == 3:
                try:
                    return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
                except ValueError:
                    pass
            elif len(parts) == 2:
                try:
                    return int(parts[0]) * 60 + int(parts[1])
                except ValueError:
                    pass

        # 尝试解析自然语言
        hours = re.search(r"(\d+)\s*hour", duration_str, re.I)
        minutes = re.search(r"(\d+)\s*min", duration_str, re.I)
        seconds = re.search(r"(\d+)\s*sec", duration_str, re.I)

        total = 0
        if hours:
            total += int(hours.group(1)) * 3600
        if minutes:
            total += int(minutes.group(1)) * 60
        if seconds:
            total += int(seconds.group(1))

        return total if total > 0 else None


# 全局单例
_rss_source: Optional[RSSSource] = None


def get_rss_source() -> RSSSource:
    """获取RSS来源单例"""
    global _rss_source
    if _rss_source is None:
        _rss_source = RSSSource()
    return _rss_source
