"""相等性工具"""

from typing import Optional, Any


class EqualityTool:
    """相等性工具"""

    def equals(self, a: Any, b: Any) -> bool:
        """是否相等"""
        return a == b

    def not_equals(self, a: Any, b: Any) -> bool:
        """是否不等"""
        return a != b


_tool: Optional[EqualityTool] = None


def get_equality_tool() -> EqualityTool:
    global _tool
    if _tool is None:
        _tool = EqualityTool()
    return _tool