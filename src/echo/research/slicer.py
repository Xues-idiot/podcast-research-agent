"""切片工具"""

from typing import Optional, Any


class SlicerTool:
    """切片工具"""

    def slice(self, items: list, start: int = 0, end: int = None) -> list:
        """切片"""
        return items[start:end]

    def take(self, items: list, count: int) -> list:
        """取前n个"""
        return items[:count]

    def drop(self, items: list, count: int) -> list:
        """跳过前n个"""
        return items[count:]


_slicer: Optional[SlicerTool] = None


def get_slicer_tool() -> SlicerTool:
    global _slicer
    if _slicer is None:
        _slicer = SlicerTool()
    return _slicer