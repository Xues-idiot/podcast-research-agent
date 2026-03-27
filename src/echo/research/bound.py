"""绑定工具"""

from typing import Optional, Any


class BoundTool:
    """绑定工具"""

    def bound(self, value: float, min_val: float, max_val: float) -> float:
        """限制在范围内"""
        return max(min_val, min(max_val, value))

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        """限制"""
        return self.bounded(value, min_val, max_val)


_tool: Optional[BoundTool] = None


def get_bound_tool() -> BoundTool:
    global _tool
    if _tool is None:
        _tool = BoundTool()
    return _tool