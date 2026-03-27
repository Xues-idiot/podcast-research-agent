"""相等性工具"""

from typing import Optional, Any


class EqualityTool:
    """相等性工具"""

    def equals(self, a: Any, b: Any) -> bool:
        """判断相等"""
        return a == b

    def not_equals(self, a: Any, b: Any) -> bool:
        """判断不相等"""
        return a != b


_equality_tool: Optional[EqualityTool] = None


def get_equality_tool() -> EqualityTool:
    global _equality_tool
    if _equality_tool is None:
        _equality_tool = EqualityTool()
    return _equality_tool