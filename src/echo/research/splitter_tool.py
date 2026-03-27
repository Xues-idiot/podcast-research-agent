"""分割工具"""

from typing import Optional, Any


class SplitterTool:
    """分割工具"""

    def split(self, text: str, delimiter: str) -> list:
        """分割"""
        return text.split(delimiter)

    def split_once(self, text: str, delimiter: str) -> tuple:
        """分割一次"""
        parts = text.split(delimiter, 1)
        if len(parts) == 1:
            return (parts[0], "")
        return (parts[0], parts[1])


_splitter: Optional[SplitterTool] = None


def get_splitter_tool() -> SplitterTool:
    global _splitter
    if _splitter is None:
        _splitter = SplitterTool()
    return _splitter