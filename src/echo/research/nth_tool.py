"""第N个元素工具"""

from typing import Optional, List, Any


class NthTool:
    """第N个元素工具"""

    def nth(self, items: List[Any], n: int) -> Any:
        """第n个元素"""
        return items[n] if 0 <= n < len(items) else None


_nth_tool: Optional[NthTool] = None


def get_nth_tool() -> NthTool:
    global _nth_tool
    if _nth_tool is None:
        _nth_tool = NthTool()
    return _nth_tool