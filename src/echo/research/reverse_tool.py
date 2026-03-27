"""反转工具"""

from typing import Optional, List, Any


class ReverseTool:
    """反转工具"""

    def reverse(self, items: List[Any]) -> List[Any]:
        """反转"""
        return list(reversed(items))


_reverse_tool: Optional[ReverseTool] = None


def get_reverse_tool() -> ReverseTool:
    global _reverse_tool
    if _reverse_tool is None:
        _reverse_tool = ReverseTool()
    return _reverse_tool