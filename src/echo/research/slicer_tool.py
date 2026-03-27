"""切片工具"""

from typing import Optional, List, Any


class SlicerTool:
    """切片工具"""

    def slice(self, items: List[Any], start: int, end: int = None) -> List[Any]:
        """切片"""
        return items[start:end]


_slicer_tool: Optional[SlicerTool] = None


def get_slicer_tool() -> SlicerTool:
    global _slicer_tool
    if _slicer_tool is None:
        _slicer_tool = SlicerTool()
    return _slicer_tool