"""剪贴板导入器 - 从剪贴板快速导入播客URL"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedURL:
    """解析后的URL"""
    url: str
    platform: str = ""
    is_valid: bool = False
    title: str = ""


class ClipboardImporter:
    """剪贴板导入器"""

    # 支持的平台模式
    PLATFORM_PATTERNS = {
        "youtube": [
            r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+",
            r"(?:https?://)?(?:www\.)?youtu\.be/[\w-]+",
        ],
        "bilibili": [
            r"(?:https?://)?(?:www\.)?bilibili\.com/video/[Bb][Vv][\w]+",
            r"(?:https?://)?b23\.tv/[\w]+",
        ],
        "xiaohongshu": [
            r"(?:https?://)?(?:www\.)?xiaohongshu\.com/discovery/item/[\w]+",
        ],
        "ximalaya": [
            r"(?:https?://)?(?:www\.)?ximalaya\.com/[^\s]+",
        ],
        "xiaoyuanzhou": [
            r"(?:https?://)?(?:www\.)?xiaoyuanzhou\.fm/[^\s]+",
        ],
        "rss": [
            r"(?:https?://)?[^\s]+\.rss",
            r"(?:https?://)?[^\s]+/feed",
        ],
    }

    def parse(self, text: str) -> list[ParsedURL]:
        """解析剪贴板文本中的URL

        Args:
            text: 剪贴板文本

        Returns:
            解析后的URL列表
        """
        urls = []

        # 提取所有URL
        url_pattern = r"https?://[^\s<>'\"{}|\\^`\[\]]+"
        matches = re.findall(url_pattern, text)

        for url in matches:
            parsed = self._identify_platform(url)
            urls.append(parsed)

        return urls

    def _identify_platform(self, url: str) -> ParsedURL:
        """识别URL平台

        Args:
            url: URL

        Returns:
            解析后的URL
        """
        url_lower = url.lower()

        for platform, patterns in self.PLATFORM_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, url_lower, re.IGNORECASE):
                    return ParsedURL(
                        url=url,
                        platform=platform,
                        is_valid=True,
                    )

        # 检查是否是通用RSS
        if "rss" in url_lower or "feed" in url_lower:
            return ParsedURL(
                url=url,
                platform="rss",
                is_valid=True,
            )

        return ParsedURL(
            url=url,
            platform="unknown",
            is_valid=False,
        )

    def is_valid_podcast_url(self, url: str) -> bool:
        """检查是否是有效的播客URL

        Args:
            url: URL

        Returns:
            是否有效
        """
        parsed = self._identify_platform(url)
        return parsed.is_valid

    def get_platform_from_url(self, url: str) -> str:
        """从URL获取平台

        Args:
            url: URL

        Returns:
            平台名称
        """
        parsed = self._identify_platform(url)
        return parsed.platform


# 全局实例
_clipboard_importer: Optional[ClipboardImporter] = None


def get_clipboard_importer() -> ClipboardImporter:
    """获取全局剪贴板导入器"""
    global _clipboard_importer
    if _clipboard_importer is None:
        _clipboard_importer = ClipboardImporter()
    return _clipboard_importer
