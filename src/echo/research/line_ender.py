"""行结束符工具"""

from typing import Optional


class LineEnder:
    """行结束符工具"""

    def to_unix(self, text: str) -> str:
        """转换为Unix格式(LF)"""
        return text.replace("\r\n", "\n").replace("\r", "\n")

    def to_windows(self, text: str) -> str:
        """转换为Windows格式(CRLF)"""
        return self.to_unix(text).replace("\n", "\r\n")

    def to_mac(self, text: str) -> str:
        """转换为Mac格式(CR)"""
        return text.replace("\r\n", "\r").replace("\n", "\r")


_ender: Optional[LineEnder] = None


def get_line_ender() -> LineEnder:
    global _ender
    if _ender is None:
        _ender = LineEnder()
    return _ender