"""偏移工具"""

from typing import Optional


class OffsetTool:
    """偏移工具"""

    def offset(self, value: float, delta: float) -> float:
        """偏移值"""
        return value + delta

    def scale(self, value: float, factor: float) -> float:
        """缩放值"""
        return value * factor


_tool: Optional[OffsetTool] = None


def get_offset_tool() -> OffsetTool:
    global _tool
    if _tool is None:
        _tool = OffsetTool()
    return _tool