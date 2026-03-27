"""窗口制造工具"""

from typing import Optional, List, Any


class WindowMakerTool:
    """窗口制造工具"""

    def make_window(self, items: List[Any], size: int) -> List[List[Any]]:
        """制造窗口"""
        return [items[i:i+size] for i in range(len(items) - size + 1)]


_window_maker_tool: Optional[WindowMakerTool] = None


def get_window_maker_tool() -> WindowMakerTool:
    global _window_maker_tool
    if _window_maker_tool is None:
        _window_maker_tool = WindowMakerTool()
    return _window_maker_tool