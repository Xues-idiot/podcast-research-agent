"""最大值工具"""

from typing import Optional, List, Any


class MaxTool:
    """最大值工具"""

    def max_value(self, items: List[Any]) -> Any:
        """最大值"""
        return max(items) if items else None


_max_tool: Optional[MaxTool] = None


def get_max_tool() -> MaxTool:
    global _max_tool
    if _max_tool is None:
        _max_tool = MaxTool()
    return _max_tool