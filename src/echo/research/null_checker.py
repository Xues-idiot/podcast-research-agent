"""空值检查工具"""

from typing import Optional, Any


class NullCheckerTool:
    """空值检查工具"""

    def is_none(self, value: Any) -> bool:
        """检查是否为None"""
        return value is None

    def is_empty(self, value: Any) -> bool:
        """检查是否为空"""
        if value is None:
            return True
        if isinstance(value, (str, list, dict, tuple, set)):
            return len(value) == 0
        return False

    def is_none_or_empty(self, value: Any) -> bool:
        """检查是否为None或空"""
        return self.is_none(value) or self.is_empty(value)


_null_checker_tool: Optional[NullCheckerTool] = None


def get_null_checker_tool() -> NullCheckerTool:
    global _null_checker_tool
    if _null_checker_tool is None:
        _null_checker_tool = NullCheckerTool()
    return _null_checker_tool