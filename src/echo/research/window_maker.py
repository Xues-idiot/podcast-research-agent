"""窗口工具"""

from typing import Optional, Any


class WindowMaker:
    """窗口工具"""

    def sliding_window(self, items: list, size: int) -> list:
        """滑动窗口"""
        return [items[i:i+size] for i in range(len(items) - size + 1)]

    def windowed(self, items: list, size: int) -> list:
        """窗口化"""
        return self.sliding_window(items, size)


_maker: Optional[WindowMaker] = None


def get_window_maker() -> WindowMaker:
    global _maker
    if _maker is None:
        _maker = WindowMaker()
    return _maker