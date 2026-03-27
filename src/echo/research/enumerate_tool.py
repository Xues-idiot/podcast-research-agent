"""枚举工具"""

from typing import Optional, List, Any


class EnumerateTool:
    """枚举工具"""

    def enumerate_items(self, items: List[Any], start: int = 0) -> List[tuple]:
        """枚举"""
        return list(enumerate(items, start))


_enumerate_tool: Optional[EnumerateTool] = None


def get_enumerate_tool() -> EnumerateTool:
    global _enumerate_tool
    if _enumerate_tool is None:
        _enumerate_tool = EnumerateTool()
    return _enumerate_tool