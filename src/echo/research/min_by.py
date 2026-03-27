"""按键最小最大工具"""

from typing import List, Any, Callable, Optional


class MinBy:
    _instance: Optional["MinBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def min_by(self, items: List[Any], key: Callable) -> Any:
        if not items:
            return None
        return min(items, key=key)

    def max_by(self, items: List[Any], key: Callable) -> Any:
        if not items:
            return None
        return max(items, key=key)

    def min_max_by(self, items: List[Any], key: Callable) -> tuple:
        if not items:
            return None, None
        sorted_items = sorted(items, key=key)
        return sorted_items[0], sorted_items[-1]


def get_min_by() -> MinBy:
    return MinBy()
