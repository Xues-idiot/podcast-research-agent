"""第一个元素工具"""

from typing import Optional, List, Any


class FirstTool:
    """第一个元素工具"""

    def first(self, items: List[Any]) -> Any:
        """第一个元素"""
        return items[0] if items else None


_first_tool: Optional[FirstTool] = None


def get_first_tool() -> FirstTool:
    global _first_tool
    if _first_tool is None:
        _first_tool = FirstTool()
    return _first_tool