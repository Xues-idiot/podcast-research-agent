"""相等检查工具"""

from typing import Optional, Any


class EqualTool:
    """相等检查工具"""

    def equal(self, a: Any, b: Any) -> bool:
        """检查相等"""
        return a == b


_equal_tool: Optional[EqualTool] = None


def get_equal_tool() -> EqualTool:
    global _equal_tool
    if _equal_tool is None:
        _equal_tool = EqualTool()
    return _equal_tool