"""空操作工具"""

from typing import Optional, Any


class NoOpTool:
    """空操作工具"""

    def noop(self, *args, **kwargs) -> None:
        """空操作"""
        pass


_noop_tool: Optional[NoOpTool] = None


def get_noop_tool() -> NoOpTool:
    global _noop_tool
    if _noop_tool is None:
        _noop_tool = NoOpTool()
    return _noop_tool