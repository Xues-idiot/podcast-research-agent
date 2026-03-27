"""正则表达式模式库"""

import re
from typing import Optional


class RegexPatterns:
    """常用正则表达式模式"""

    EMAIL = r'[\w.-]+@[\w.-]+\.\w+'
    PHONE_CN = r'1[3-9]\d{9}'
    URL = r'https?://\S+'
    IP_V4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    DATE_ISO = r'\d{4}-\d{2}-\d{2}'
    TIME_24H = r'\d{2}:\d{2}(:\d{2})?'
    HEX_COLOR = r'#[0-9a-fA-F]{6}'
    UUID = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    CHINESE = r'[\u4e00-\u9fff]+'
    ALPHANUMERIC = r'[a-zA-Z0-9]+'

    @classmethod
    def find_all(cls, pattern: str, text: str) -> list[str]:
        """查找所有匹配"""
        return re.findall(pattern, text)

    @classmethod
    def is_match(cls, pattern: str, text: str) -> bool:
        """是否匹配"""
        return bool(re.match(pattern, text))


_patterns: Optional[RegexPatterns] = None


def get_regex_patterns() -> RegexPatterns:
    global _patterns
    if _patterns is None:
        _patterns = RegexPatterns()
    return _patterns