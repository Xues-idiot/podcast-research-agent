"""切片工具"""

from typing import Optional, List, Any


class SliceTool:
    """切片工具"""

    def slice(self, items: List[Any], start: int = 0, end: int = None) -> List[Any]:
        """切片"""
        return items[start:end]


_slice_tool: Optional[SliceTool] = None


def get_slice_tool() -> SliceTool:
    global _slice_tool
    if _slice_tool is None:
        _slice_tool = SliceTool()
    return _slice_tool