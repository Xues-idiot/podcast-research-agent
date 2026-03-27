"""滑动窗口工具"""

from typing import Optional, List, Any


class WindowBySizeTool:
    """滑动窗口工具"""

    def window_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        """滑动窗口"""
        return [items[i:i+size] for i in range(len(items) - size + 1)]


_window_by_size_tool: Optional[WindowBySizeTool] = None


def get_window_by_size_tool() -> WindowBySizeTool:
    global _window_by_size_tool
    if _window_by_size_tool is None:
        _window_by_size_tool = WindowBySizeTool()
    return _window_by_size_tool