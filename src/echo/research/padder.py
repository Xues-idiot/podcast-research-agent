"""字符串填充工具"""

from typing import Optional


class StringPadder:
    """字符串填充工具"""

    def pad_left(self, text: str, width: int, char: str = " ") -> str:
        """左填充"""
        return text.rjust(width, char)

    def pad_right(self, text: str, width: int, char: str = " ") -> str:
        """右填充"""
        return text.ljust(width, char)

    def pad_center(self, text: str, width: int, char: str = " ") -> str:
        """居中填充"""
        return text.center(width, char)


_padder: Optional[StringPadder] = None


def get_string_padder() -> StringPadder:
    global _padder
    if _padder is None:
        _padder = StringPadder()
    return _padder