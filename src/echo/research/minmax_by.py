"""最小最大工具"""

from typing import List, Any, Callable, Tuple, Optional


class MinMaxBy:
    _instance: Optional["MinMaxBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def min_by(self, items: List[Any], key_func: Callable = None) -> Any:
        if not items:
            return None
        if key_func is None:
            return min(items)
        return min(items, key=key_func)

    def max_by(self, items: List[Any], key_func: Callable = None) -> Any:
        if not items:
            return None
        if key_func is None:
            return max(items)
        return max(items, key=key_func)


def get_minmax_by() -> MinMaxBy:
    return MinMaxBy()
