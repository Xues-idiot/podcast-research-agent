"""三元表达式工具"""

from typing import Optional, Any


class TernaryTool:
    """三元表达式工具"""

    def if_then_else(self, condition: bool, then_val: Any, else_val: Any) -> Any:
        """三元表达式"""
        return then_val if condition else else_val


_ternary_tool: Optional[TernaryTool] = None


def get_ternary_tool() -> TernaryTool:
    global _ternary_tool
    if _ternary_tool is None:
        _ternary_tool = TernaryTool()
    return _ternary_tool