"""字符串构建工具"""

from typing import Optional


class StringBuilder:
    """字符串构建工具"""

    def __init__(self):
        self._parts = []

    def append(self, text: str) -> 'StringBuilder':
        """追加"""
        self._parts.append(text)
        return self

    def append_line(self, text: str = "") -> 'StringBuilder':
        """追加行"""
        self._parts.append(text + "\n")
        return self

    def to_string(self) -> str:
        """转字符串"""
        return "".join(self._parts)

    def clear(self) -> 'StringBuilder':
        """清空"""
        self._parts = []
        return self


_builder: Optional[StringBuilder] = None


def get_string_builder() -> StringBuilder:
    global _builder
    if _builder is None:
        _builder = StringBuilder()
    return _builder