"""比较工具"""

from typing import Optional, Any


class ComparatorTool:
    """比较工具"""

    def equal(self, a: Any, b: Any) -> bool:
        """相等"""
        return a == b

    def greater(self, a: Any, b: Any) -> bool:
        """大于"""
        return a > b

    def less(self, a: Any, b: Any) -> bool:
        """小于"""
        return a < b

    def between(self, value: Any, low: Any, high: Any) -> bool:
        """在范围内"""
        return low <= value <= high


_comparator_tool: Optional[ComparatorTool] = None


def get_comparator_tool() -> ComparatorTool:
    global _comparator_tool
    if _comparator_tool is None:
        _comparator_tool = ComparatorTool()
    return _comparator_tool