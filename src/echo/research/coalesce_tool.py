"""合并工具"""

from typing import Optional, Any


class CoalesceTool:
    """合并工具"""

    def coalesce(self, *values) -> Any:
        """返回第一个非None值"""
        for value in values:
            if value is not None:
                return value
        return None


_coalesce_tool: Optional[CoalesceTool] = None


def get_coalesce_tool() -> CoalesceTool:
    global _coalesce_tool
    if _coalesce_tool is None:
        _coalesce_tool = CoalesceTool()
    return _coalesce_tool