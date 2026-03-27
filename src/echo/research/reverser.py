"""反转工具"""

from typing import Optional, Any


class ReverserTool:
    """反转工具"""

    def reverse(self, items: list) -> list:
        """反转"""
        return items[::-1]

    def reverse_string(self, text: str) -> str:
        """反转字符串"""
        return text[::-1]


_reverser: Optional[ReverserTool] = None


def get_reverser_tool() -> ReverserTool:
    global _reverser
    if _reverser is None:
        _reverser = ReverserTool()
    return _reverser