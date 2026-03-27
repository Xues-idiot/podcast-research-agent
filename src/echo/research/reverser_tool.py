"""反转工具"""

from typing import Optional, List, Any


class ReverserTool:
    """反转工具"""

    def reverse(self, items: List[Any]) -> List[Any]:
        """反转"""
        return list(reversed(items))


_reverser_tool: Optional[ReverserTool] = None


def get_reverser_tool() -> ReverserTool:
    global _reverser_tool
    if _reverser_tool is None:
        _reverser_tool = ReverserTool()
    return _reverser_tool