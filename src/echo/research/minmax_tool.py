"""最小最大工具"""

from typing import Optional, List


class MinMaxTool:
    """最小最大工具"""

    def min_value(self, items: List[float]) -> float:
        """最小值"""
        return min(items) if items else 0

    def max_value(self, items: List[float]) -> float:
        """最大值"""
        return max(items) if items else 0

    def min_max(self, items: List[float]) -> tuple:
        """最小最大值"""
        return (self.min_value(items), self.max_value(items))


_minmax_tool: Optional[MinMaxTool] = None


def get_minmax_tool() -> MinMaxTool:
    global _minmax_tool
    if _minmax_tool is None:
        _minmax_tool = MinMaxTool()
    return _minmax_tool