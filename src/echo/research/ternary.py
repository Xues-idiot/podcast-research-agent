"""三元表达式工具"""

from typing import Optional, Any


class TernaryTool:
    """三元表达式工具"""

    def if_(self, condition: bool, true_val: Any, false_val: Any) -> Any:
        """三元表达式"""
        return true_val if condition else false_val


_tool: Optional[TernaryTool] = None


def get_ternary_tool() -> TernaryTool:
    global _tool
    if _tool is None:
        _tool = TernaryTool()
    return _tool