"""逻辑工具"""

from typing import Optional, Any


class LogicalTool:
    """逻辑工具"""

    def and_(self, *args) -> bool:
        """逻辑与"""
        return all(args)

    def or_(self, *args) -> bool:
        """逻辑或"""
        return any(args)

    def not_(self, value: Any) -> bool:
        """逻辑非"""
        return not value


_logical_tool: Optional[LogicalTool] = None


def get_logical_tool() -> LogicalTool:
    global _logical_tool
    if _logical_tool is None:
        _logical_tool = LogicalTool()
    return _logical_tool