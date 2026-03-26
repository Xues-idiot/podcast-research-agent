"""URL解析器增强"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedURL:
    """解析后的URL"""
    url: str
    platform: str
    is_valid: bool
    video_id: str = ""


class URLParser:
    """URL解析器"""

    PATTERNS = {
        "youtube": [
            (r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([\w-]+)", "video_id"),
            (r"(?:https?://)?(?:www\.)?youtu\.be/([\w-]+)", "video_id"),
        ],
        "bilibili": [
            (r"(?:https?://)?(?:www\.)?bilibili\.com/video/([Bb][Vv][\w]+)", "bvid"),
            (r"(?:https?://)?b23\.tv/([\w]+)", "short_id"),
        ],
        "xiaohongshu": [
            (r"(?:https?://)?(?:www\.)?xiaohongshu\.com/discovery/item/([\w]+)", "note_id"),
        ],
    }

    def parse(self, url: str) -> ParsedURL:
        for platform, patterns in self.PATTERNS.items():
            for pattern, id_type in patterns:
                match = re.search(pattern, url, re.IGNORECASE)
                if match:
                    return ParsedURL(
                        url=url,
                        platform=platform,
                        is_valid=True,
                        video_id=match.group(1) if match.groups() else "",
                    )
        return ParsedURL(url=url, platform="unknown", is_valid=False)


_parser: Optional[URLParser] = None

def get_url_parser() -> URLParser:
    global _parser
    if _parser is None:
        _parser = URLParser()
    return _parser
