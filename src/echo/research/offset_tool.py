"""偏移工具"""

from typing import Optional, List


class OffsetTool:
    """偏移工具"""

    def offset_value(self, value: float, delta: float) -> float:
        """偏移值"""
        return value + delta

    def offset_list(self, items: List[float], delta: float) -> List[float]:
        """偏移列表"""
        return [x + delta for x in items]


_offset_tool: Optional[OffsetTool] = None


def get_offset_tool() -> OffsetTool:
    global _offset_tool
    if _offset_tool is None:
        _offset_tool = OffsetTool()
    return _offset_tool