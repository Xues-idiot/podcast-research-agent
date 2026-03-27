"""偏函数工具"""

from functools import partial
from typing import Optional, Callable, Any


class PartialTool:
    """偏函数工具"""

    def partial(self, func: Callable, **defaults) -> Callable:
        """创建偏函数"""
        return partial(func, **defaults)


_tool: Optional[PartialTool] = None


def get_partial_tool() -> PartialTool:
    global _tool
    if _tool is None:
        _tool = PartialTool()
    return _tool