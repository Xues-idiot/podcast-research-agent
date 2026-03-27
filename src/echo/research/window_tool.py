"""窗口工具"""

from typing import Optional, Any


class WindowTool:
    """窗口工具"""

    def sliding_window(self, items: list, size: int) -> list:
        """滑动窗口"""
        return [items[i:i+size] for i in range(len(items) - size + 1)]

    def moving_average(self, items: list, window: int) -> list:
        """移动平均"""
        if len(items) < window:
            return []
        return [sum(items[i:i+window])/window for i in range(len(items) - window + 1)]


_tool: Optional[WindowTool] = None


def get_window_tool() -> WindowTool:
    global _tool
    if _tool is None:
        _tool = WindowTool()
    return _tool