"""逻辑操作工具"""

from typing import Optional


class LogicalTool:
    """逻辑操作工具"""

    def and_(self, a: bool, b: bool) -> bool:
        """与"""
        return a and b

    def or_(self, a: bool, b: bool) -> bool:
        """或"""
        return a or b

    def not_(self, a: bool) -> bool:
        """非"""
        return not a

    def xor(self, a: bool, b: bool) -> bool:
        """异或"""
        return bool(a) != bool(b)


_tool: Optional[LogicalTool] = None


def get_logical_tool() -> LogicalTool:
    global _tool
    if _tool is None:
        _tool = LogicalTool()
    return _tool