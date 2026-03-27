"""区间工具"""

from typing import Optional, Tuple


class RangeTool:
    """区间工具"""

    def is_in_range(self, value: float, min_val: float, max_val: float) -> bool:
        """是否在范围内"""
        return min_val <= value <= max_val

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        """限制在范围内"""
        return max(min_val, min(max_val, value))


_tool: Optional[RangeTool] = None


def get_range_tool() -> RangeTool:
    global _tool
    if _tool is None:
        _tool = RangeTool()
    return _tool