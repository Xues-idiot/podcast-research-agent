"""条件排序工具"""

from typing import List, Any, Callable, Optional


class SortPred:
    _instance: Optional["SortPred"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sort_by(self, items: List[Any], key: Callable, reverse: bool = False) -> List[Any]:
        return sorted(items, key=key, reverse=reverse)

    def sort_with(self, items: List[Any], comp: Callable) -> List[Any]:
        return sorted(items, key=comp)


def get_sort_pred() -> SortPred:
    return SortPred()
