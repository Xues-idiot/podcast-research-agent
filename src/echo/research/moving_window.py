"""滑动窗口工具"""

from typing import List, Any, Optional


class MovingWindow:
    _instance: Optional["MovingWindow"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def windowed(self, items: List[Any], size: int) -> List[List[Any]]:
        if size <= 0 or size > len(items):
            return []
        return [items[i:i+size] for i in range(len(items) - size + 1)]


def get_moving_window() -> MovingWindow:
    return MovingWindow()
