"""选择工具"""

from typing import Optional, List, Any


class SelectorTool:
    """选择工具"""

    def first(self, items: List[Any]) -> Any:
        """第一个元素"""
        return items[0] if items else None

    def last(self, items: List[Any]) -> Any:
        """最后一个元素"""
        return items[-1] if items else None

    def nth(self, items: List[Any], n: int) -> Any:
        """第n个元素"""
        return items[n] if 0 <= n < len(items) else None


_selector_tool: Optional[SelectorTool] = None


def get_selector_tool() -> SelectorTool:
    global _selector_tool
    if _selector_tool is None:
        _selector_tool = SelectorTool()
    return _selector_tool