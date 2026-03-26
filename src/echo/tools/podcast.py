"""播客RSS解析器"""

import asyncio
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from urllib.parse import urlparse

import feedparser


@dataclass
class PodcastEpisode:
    """播客单集"""
    title: str
    url: str
    description: str
    published: Optional[datetime]
    duration: Optional[str]
    audio_url: str


class PodcastRSSParser:
    """
    播客RSS解析器 - 解析播客订阅源

    支持标准RSS 2.0格式的播客
    """

    def __init__(self):
        pass

    async def parse(self, rss_url: str) -> List[PodcastEpisode]:
        """
        解析RSS获取所有剧集

        Args:
            rss_url: 播客RSS地址

        Returns:
            剧集列表
        """
        episodes = await asyncio.run_in_executor(
            None,
            lambda: self._parse_sync(rss_url)
        )
        return episodes

    def _parse_sync(self, rss_url: str) -> List[PodcastEpisode]:
        """同步解析RSS"""
        feed = feedparser.parse(rss_url)

        episodes = []
        for entry in feed.entries:
            # 提取音频URL
            audio_url = ""
            if hasattr(entry, "enclosures") and entry.enclosures:
                audio_url = entry.enclosures[0].get("href", "")

            # 解析发布时间
            published = None
            if hasattr(entry, "published_parsed") and entry.published_parsed and len(entry.published_parsed) >= 6:
                published = datetime(*entry.published_parsed[:6])

            episode = PodcastEpisode(
                title=entry.get("title", ""),
                url=entry.get("link", ""),
                description=entry.get("description", ""),
                published=published,
                duration=self._get_duration(entry),
                audio_url=audio_url,
            )
            episodes.append(episode)

        return episodes

    def _get_duration(self, entry) -> Optional[str]:
        """获取时长"""
        if hasattr(entry, "itunes_duration"):
            return str(entry.itunes_duration)
        return None

    def get_latest(self, rss_url: str, num: int = 5) -> List[PodcastEpisode]:
        """
        获取最新N集

        Args:
            rss_url: RSS地址
            num: 获取数量

        Returns:
            最新剧集列表
        """
        episodes = self._parse_sync(rss_url)
        return episodes[:num]
