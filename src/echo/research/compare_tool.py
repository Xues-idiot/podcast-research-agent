"""比较工具"""

from typing import Optional, Any


class CompareTool:
    """比较工具"""

    def greater_than(self, a: Any, b: Any) -> bool:
        """大于"""
        return a > b

    def less_than(self, a: Any, b: Any) -> bool:
        """小于"""
        return a < b

    def equal(self, a: Any, b: Any) -> bool:
        """等于"""
        return a == b


_compare_tool: Optional[CompareTool] = None


def get_compare_tool() -> CompareTool:
    global _compare_tool
    if _compare_tool is None:
        _compare_tool = CompareTool()
    return _compare_tool