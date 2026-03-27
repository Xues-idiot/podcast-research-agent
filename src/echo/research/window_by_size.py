"""按大小窗口工具"""

from typing import Callable, List, Optional, TypeVar


T = TypeVar("T")


class WindowBySize:
    _instance: Optional["WindowBySize"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def window(self, items: List[T], size: int, step: int = 1) -> List[List[T]]:
        result = []
        for i in range(0, len(items) - size + 1, step):
            result.append(items[i:i + size])
        return result

    def window_with_padding(self, items: List[T], size: int, pad: T) -> List[List[T]]:
        result = []
        for i in range(0, len(items), size):
            window = items[i:i + size]
            if len(window) < size:
                window = window + [pad] * (size - len(window))
            result.append(window)
        return result


def get_window_by_size() -> WindowBySize:
    return WindowBySize()
