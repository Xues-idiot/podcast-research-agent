"""最小值工具"""

from typing import Optional, List, Any


class MinTool:
    """最小值工具"""

    def min_value(self, items: List[Any]) -> Any:
        """最小值"""
        return min(items) if items else None


_min_tool: Optional[MinTool] = None


def get_min_tool() -> MinTool:
    global _min_tool
    if _min_tool is None:
        _min_tool = MinTool()
    return _min_tool