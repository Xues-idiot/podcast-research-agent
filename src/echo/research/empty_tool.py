"""空值工具"""

from typing import Optional, Any


class EmptyTool:
    """空值工具"""

    def is_empty(self, value: Any) -> bool:
        """是否为空"""
        if value is None:
            return True
        if isinstance(value, (str, list, dict, tuple, set)):
            return len(value) == 0
        return False


_empty_tool: Optional[EmptyTool] = None


def get_empty_tool() -> EmptyTool:
    global _empty_tool
    if _empty_tool is None:
        _empty_tool = EmptyTool()
    return _empty_tool