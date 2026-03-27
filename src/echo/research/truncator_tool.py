"""字符串截断工具"""

from typing import Optional


class StringTruncator:
    """字符串截断工具"""

    def truncate(self, text: str, max_length: int, suffix: str = "...") -> str:
        """截断"""
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix

    def truncate_middle(self, text: str, max_length: int, separator: str = "...") -> str:
        """中间截断"""
        if len(text) <= max_length:
            return text
        half = (max_length - len(separator)) // 2
        return text[:half] + separator + text[-half:]


_truncator: Optional[StringTruncator] = None


def get_string_truncator() -> StringTruncator:
    global _truncator
    if _truncator is None:
        _truncator = StringTruncator()
    return _truncator