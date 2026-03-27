"""最小最大工具"""

from typing import Optional, Any


class MinMaxTool:
    """最小最大工具"""

    def min_of(self, *values) -> Any:
        """最小值"""
        return min(values)

    def max_of(self, *values) -> Any:
        """最大值"""
        return max(values)


_tool: Optional[MinMaxTool] = None


def get_minmax_tool() -> MinMaxTool:
    global _tool
    if _tool is None:
        _tool = MinMaxTool()
    return _tool