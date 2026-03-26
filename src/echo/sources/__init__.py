"""多源聚合模块

支持从多个平台聚合播客内容：
- YouTube
- Bilibili
- 小宇宙
- 喜马拉雅
- 通用 RSS

每个来源有统一的接口，便于扩展新的来源。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class SourceType(Enum):
    """来源类型"""
    YOUTUBE = "youtube"
    BILIBILI = "bilibili"
    XIAOYUANZHOU = "xiaoyuanzhou"  # 小宇宙
    XIMALAYA = "ximalaya"  # 喜马拉雅
    RSS = "rss"
    UNKNOWN = "unknown"


@dataclass
class PodcastEpisode:
    """播客剧集"""
    source: SourceType
    source_id: str  # 平台原始ID
    title: str
    description: str
    audio_url: str
    thumbnail_url: Optional[str] = None
    duration: Optional[int] = None  # 秒
    published_at: Optional[str] = None  # ISO格式
    metadata: dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

    @property
    def source_name(self) -> str:
        """获取来源名称"""
        names = {
            SourceType.YOUTUBE: "YouTube",
            SourceType.BILIBILI: "Bilibili",
            SourceType.XIAOYUANZHOU: "小宇宙",
            SourceType.XIMALAYA: "喜马拉雅",
            SourceType.RSS: "RSS",
            SourceType.UNKNOWN: "未知来源",
        }
        return names.get(self.source, "未知来源")


@dataclass
class PodcastChannel:
    """播客频道"""
    source: SourceType
    source_id: str
    title: str
    description: str
    feed_url: str  # RSS feed URL
    thumbnail_url: Optional[str] = None
    episodes: list[PodcastEpisode] = None
    metadata: dict = None

    def __post_init__(self):
        if self.episodes is None:
            self.episodes = []
        if self.metadata is None:
            self.metadata = {}


class BaseSource(ABC):
    """播客来源基类"""

    @property
    @abstractmethod
    def source_type(self) -> SourceType:
        """来源类型"""
        pass

    @abstractmethod
    async def get_channel(self, url: str) -> PodcastChannel:
        """获取频道信息

        Args:
            url: 频道/播客URL

        Returns:
            PodcastChannel
        """
        pass

    @abstractmethod
    async def get_episode(self, url: str) -> PodcastEpisode:
        """获取单集信息

        Args:
            url: 剧集URL

        Returns:
            PodcastEpisode
        """
        pass

    @abstractmethod
    async def get_audio_url(self, episode: PodcastEpisode) -> str:
        """获取音频URL

        Args:
            episode: 剧集信息

        Returns:
            音频直链
        """
        pass

    @abstractmethod
    def detect_source(self, url: str) -> bool:
        """检测URL是否属于此来源

        Args:
            url: 待检测URL

        Returns:
            True if URL matches this source
        """
        pass


def detect_source_type(url: str) -> SourceType:
    """检测URL的来源类型

    Args:
        url: 待检测URL

    Returns:
        SourceType
    """
    url_lower = url.lower()

    # YouTube
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        return SourceType.YOUTUBE

    # Bilibili
    if "bilibili.com" in url_lower or "b23.tv" in url_lower:
        return SourceType.BILIBILI

    # 小宇宙
    if "xiaoyuanzhou" in url_lower or "xiaoyuanzhou.fm" in url_lower:
        return SourceType.XIAOYUANZHOU

    # 喜马拉雅
    if "ximalaya" in url_lower or "喜马拉雅" in url:
        return SourceType.XIMALAYA

    # RSS
    if ".xml" in url_lower or ".rss" in url_lower or "feed" in url_lower:
        return SourceType.RSS

    return SourceType.UNKNOWN


class SourceRegistry:
    """来源注册表

    管理所有已注册的来源，支持来源发现和路由
    """

    def __init__(self):
        self._sources: dict[SourceType, BaseSource] = {}

    def register(self, source: BaseSource):
        """注册来源"""
        self._sources[source.source_type] = source

    def get(self, source_type: SourceType) -> Optional[BaseSource]:
        """获取来源处理器"""
        return self._sources.get(source_type)

    def detect_and_get(self, url: str) -> tuple[SourceType, Optional[BaseSource]]:
        """检测URL类型并获取处理器

        Returns:
            (SourceType, Source or None)
        """
        source_type = detect_source_type(url)
        source = self.get(source_type)
        return source_type, source

    def list_sources(self) -> list[SourceType]:
        """列出所有已注册的来源"""
        return list(self._sources.keys())


# 全局来源注册表
_registry = SourceRegistry()


def get_registry() -> SourceRegistry:
    """获取全局来源注册表"""
    return _registry


def register_source(source: BaseSource):
    """注册来源到全局注册表"""
    _registry.register(source)


# 便捷导入
from echo.sources.youtube import YouTubeSource, get_youtube_source
from echo.sources.bilibili import BilibiliSource, get_bilibili_source
from echo.sources.rss import RSSSource, get_rss_source
from echo.sources.xiaoyuanzhou import XiaoyuanzhouSource, get_xiaoyuanzhou_source
from echo.sources.ximalaya import XimalayaSource, get_ximalaya_source

__all__ = [
    # 类型
    "SourceType",
    "PodcastEpisode",
    "PodcastChannel",
    # 基类
    "BaseSource",
    # 工具函数
    "detect_source_type",
    # 注册表
    "SourceRegistry",
    "get_registry",
    "register_source",
    # 具体来源
    "YouTubeSource",
    "get_youtube_source",
    "BilibiliSource",
    "get_bilibili_source",
    "RSSSource",
    "get_rss_source",
    "XiaoyuanzhouSource",
    "get_xiaoyuanzhou_source",
    "XimalayaSource",
    "get_ximalaya_source",
]


def register_all_sources():
    """注册所有内置来源到全局注册表"""
    register_source(get_youtube_source())
    register_source(get_bilibili_source())
    register_source(get_rss_source())
    register_source(get_xiaoyuanzhou_source())
    register_source(get_ximalaya_source())
