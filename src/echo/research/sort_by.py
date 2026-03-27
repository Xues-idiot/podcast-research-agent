"""排序工具"""

from typing import List, Any, Callable, Optional


class SortBy:
    _instance: Optional["SortBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sort_by(self, items: List[Any], key_func: Callable = None, reverse: bool = False) -> List[Any]:
        return sorted(items, key=key_func, reverse=reverse)


def get_sort_by() -> SortBy:
    return SortBy()
