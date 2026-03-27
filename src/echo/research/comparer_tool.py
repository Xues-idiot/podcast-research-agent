"""比较工具"""

from typing import Optional, Any


class ComparerTool:
    """比较工具"""

    def compare(self, a: Any, b: Any) -> int:
        """比较: -1, 0, 1"""
        if a < b:
            return -1
        if a > b:
            return 1
        return 0


_comparer_tool: Optional[ComparerTool] = None


def get_comparer_tool() -> ComparerTool:
    global _comparer_tool
    if _comparer_tool is None:
        _comparer_tool = ComparerTool()
    return _comparer_tool