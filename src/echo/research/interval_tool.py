"""区间工具"""

from typing import Optional, Tuple


class IntervalTool:
    """区间工具"""

    def in_interval(self, value: float, low: float, high: float) -> bool:
        """检查值是否在区间内"""
        return low <= value <= high

    def clamp(self, value: float, low: float, high: float) -> float:
        """限制值在区间内"""
        return max(low, min(value, high))

    def overlap(self, a: Tuple[float, float], b: Tuple[float, float]) -> bool:
        """检查区间是否重叠"""
        return a[0] <= b[1] and b[0] <= a[1]


_interval_tool: Optional[IntervalTool] = None


def get_interval_tool() -> IntervalTool:
    global _interval_tool
    if _interval_tool is None:
        _interval_tool = IntervalTool()
    return _interval_tool