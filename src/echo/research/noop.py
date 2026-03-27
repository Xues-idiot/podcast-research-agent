"""空操作工具"""

from typing import Optional, Callable, Any


class NoOpTool:
    """空操作工具"""

    def noop(self, *args, **kwargs) -> None:
        """空操作"""
        pass

    def empty_func(self) -> Callable:
        """返回空函数"""
        return self.noop


_tool: Optional[NoOpTool] = None


def get_noop_tool() -> NoOpTool:
    global _tool
    if _tool is None:
        _tool = NoOpTool()
    return _tool