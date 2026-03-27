"""调用跟踪工具"""

from typing import Optional, Callable, Any


class TapTool:
    """调用跟踪工具"""

    def tap(self, value: Any, func: Callable = None) -> Any:
        """查看并传递值"""
        if func:
            func(value)
        return value


_tool: Optional[TapTool] = None


def get_tap_tool() -> TapTool:
    global _tool
    if _tool is None:
        _tool = TapTool()
    return _tool