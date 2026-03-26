"""URL验证器"""

import re
from typing import Tuple
from urllib.parse import urlparse


class URLValidator:
    """
    URL验证器

    支持验证:
    - B站视频URL
    - YouTube视频URL
    - 抖音/火山视频URL
    - 微信公众号/视频号
    - 小红书播客RSS
    - 播客RSS URL
    """

    # B站URL模式
    BILIBILI_PATTERNS = [
        r"bilibili\.com/video/[Bb][Vv]\w+",
        r"b23\.tv/\w+",
        r"bilibili\.com/video/[Bb][Vv]\w+\?p=\d+",
    ]

    # YouTube URL模式
    YOUTUBE_PATTERNS = [
        r"youtube\.com/watch\?v=\w+",
        r"youtu\.be/\w+",
        r"youtube\.com/shorts/\w+",
        r"youtube\.com/playlist\?list=\w+",
    ]

    # 抖音/火山URL模式
    DOUYIN_PATTERNS = [
        r"douyin\.com/video/\d+",
        r"v\.douyin\.com/\w+",
        r"huoshan\.com/\w+",
    ]

    # 微信URL模式
    WECHAT_PATTERNS = [
        r"mp\.weixin\.qq\.com/s/\w+",      # 公众号文章
        r"mp\.weixin\.qq\.com/video/\w+",   # 视频
        r"channels\.weixin\.qq\.com/\w+",  # 视频号
    ]

    # 小红书URL模式
    XIAOHONGSHU_PATTERNS = [
        r"xiaohongshu\.com/explore/\w+",
        r"xhslink\.com/\w+",
    ]

    # RSS URL模式
    RSS_PATTERNS = [
        r".*\.xml",
        r".*\.rss",
        r".*feed.*",
    ]

    @classmethod
    def validate(cls, url: str) -> Tuple[bool, str]:
        """
        验证URL

        Args:
            url: 要验证的URL

        Returns:
            (是否有效, URL类型)
            - ("bilibili", "B站视频")
            - ("youtube", "YouTube视频")
            - ("douyin", "抖音/火山视频")
            - ("wechat", "微信文章/视频")
            - ("xiaohongshu", "小红书")
            - ("rss", "RSS订阅")
            - ("", "未知")
        """
        if not url:
            return False, ""

        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # 检查B站
        if "bilibili.com" in domain or "b23.tv" in domain:
            if any(re.search(p, url) for p in cls.BILIBILI_PATTERNS):
                return True, "bilibili"

        # 检查YouTube
        if "youtube.com" in domain or "youtu.be" in domain:
            if any(re.search(p, url) for p in cls.YOUTUBE_PATTERNS):
                return True, "youtube"

        # 检查抖音/火山
        if "douyin.com" in domain or "huoshan.com" in domain:
            if any(re.search(p, url) for p in cls.DOUYIN_PATTERNS):
                return True, "douyin"

        # 检查微信
        if "weixin.qq.com" in domain or "channels.weixin.qq.com" in domain:
            if any(re.search(p, url) for p in cls.WECHAT_PATTERNS):
                return True, "wechat"

        # 检查小红书
        if "xiaohongshu.com" in domain or "xhslink.com" in domain:
            if any(re.search(p, url) for p in cls.XIAOHONGSHU_PATTERNS):
                return True, "xiaohongshu"

        # 检查RSS (仅限路径末尾，避免误匹配query string中的.xml)
        if re.search(r"\.xml$|\.rss$|/feed/?$", parsed.path.lower()):
            return True, "rss"

        # 检查是否为有效HTTP URL
        if parsed.scheme in ("http", "https") and parsed.netloc:
            return True, "unknown"

        return False, ""

    @classmethod
    def get_platform(cls, url: str) -> str:
        """
        获取URL对应的平台

        Args:
            url: URL

        Returns:
            平台名称
        """
        valid, platform = cls.validate(url)
        return platform if valid else "unknown"

    @classmethod
    def is_supported(cls, url: str) -> bool:
        """
        检查URL是否支持

        Args:
            url: URL

        Returns:
            是否支持
        """
        valid, _ = cls.validate(url)
        return valid

    @classmethod
    def get_platform_display_name(cls, platform: str) -> str:
        """
        获取平台的显示名称

        Args:
            platform: 平台标识

        Returns:
            显示名称
        """
        names = {
            "bilibili": "B站",
            "youtube": "YouTube",
            "douyin": "抖音/火山",
            "wechat": "微信",
            "xiaohongshu": "小红书",
            "rss": "RSS订阅",
            "unknown": "未知来源",
        }
        return names.get(platform, "未知来源")
