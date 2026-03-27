"""空值工具"""

from typing import Optional, Any


class NullTool:
    """空值工具"""

    def is_null(self, value: Any) -> bool:
        """是否为空"""
        return value is None

    def is_empty(self, value: Any) -> bool:
        """是否为空"""
        if value is None:
            return True
        if isinstance(value, (str, list, dict, tuple, set)):
            return len(value) == 0
        return False


_tool: Optional[NullTool] = None


def get_null_tool() -> NullTool:
    global _tool
    if _tool is None:
        _tool = NullTool()
    return _tool