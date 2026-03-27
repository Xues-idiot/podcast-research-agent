"""比较操作工具"""

from typing import Optional, Any


class ComparisonTool:
    """比较操作工具"""

    def less_than(self, a: Any, b: Any) -> bool:
        """小于"""
        return a < b

    def greater_than(self, a: Any, b: Any) -> bool:
        """大于"""
        return a > b

    def less_or_equal(self, a: Any, b: Any) -> bool:
        """小于等于"""
        return a <= b

    def greater_or_equal(self, a: Any, b: Any) -> bool:
        """大于等于"""
        return a >= b


_tool: Optional[ComparisonTool] = None


def get_comparison_tool() -> ComparisonTool:
    global _tool
    if _tool is None:
        _tool = ComparisonTool()
    return _tool