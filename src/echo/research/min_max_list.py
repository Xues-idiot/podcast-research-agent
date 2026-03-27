"""最小最大工具"""

from typing import List, Any, Optional, Callable


class MinMaxList:
    _instance: Optional["MinMaxList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def min(self, items: List[Any]) -> Any:
        if not items:
            return None
        return min(items)

    def max(self, items: List[Any]) -> Any:
        if not items:
            return None
        return max(items)

    def min_max(self, items: List[Any]) -> tuple:
        if not items:
            return None, None
        return min(items), max(items)

    def min_by(self, items: List[Any], key: Callable) -> Any:
        if not items:
            return None
        return min(items, key=key)

    def max_by(self, items: List[Any], key: Callable) -> Any:
        if not items:
            return None
        return max(items, key=key)


def get_min_max_list() -> MinMaxList:
    return MinMaxList()
