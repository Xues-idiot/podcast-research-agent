"""窗口聚合工具"""

from typing import List, Any, Callable, Optional


class WindowCollect:
    _instance: Optional["WindowCollect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def window_collect(self, items: List[Any], size: int, agg: Callable) -> List[Any]:
        result = []
        for i in range(len(items) - size + 1):
            window = items[i:i + size]
            result.append(agg(window))
        return result

    def moving_avg(self, items: List[float], size: int) -> List[float]:
        return self.window_collect(items, size, lambda w: sum(w) / len(w))


def get_window_collect() -> WindowCollect:
    return WindowCollect()
