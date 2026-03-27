"""偏函数工具"""

from functools import partial
from typing import Optional, Callable, Any


class PartialTool:
    """偏函数工具"""

    def partial(self, func: Callable, *args, **kwargs) -> Callable:
        """创建偏函数"""
        return partial(func, *args, **kwargs)


_partial_tool: Optional[PartialTool] = None


def get_partial_tool() -> PartialTool:
    global _partial_tool
    if _partial_tool is None:
        _partial_tool = PartialTool()
    return _partial_tool