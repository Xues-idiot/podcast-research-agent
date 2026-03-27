"""格式化工具"""

from typing import Optional


class Formatter:
    """格式化工具"""

    def pluralize(self, count: int, singular: str, plural: str = None) -> str:
        """复数形式"""
        if plural is None:
            plural = singular + "s"
        return singular if count == 1 else plural

    def truncate_middle(self, text: str, max_length: int, ellipsis: str = "...") -> str:
        """中间截断"""
        if len(text) <= max_length:
            return text
        ellipsis_len = len(ellipsis)
        if max_length <= ellipsis_len:
            return text[:max_length]
        half = (max_length - ellipsis_len) // 2
        return text[:half] + ellipsis + text[-half:]

    def left_pad(self, text: str, width: int, char: str = " ") -> str:
        """左填充"""
        return text.rjust(width, char)


_formatter: Optional[Formatter] = None


def get_formatter() -> Formatter:
    global _formatter
    if _formatter is None:
        _formatter = Formatter()
    return _formatter