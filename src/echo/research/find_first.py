"""查找第一个工具"""

from typing import List, Any, Callable, Optional


class FindFirst:
    _instance: Optional["FindFirst"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_first(self, items: List[Any], pred: Callable) -> Any:
        for item in items:
            if pred(item):
                return item
        return None

    def find_first_index(self, items: List[Any], pred: Callable) -> int:
        for i, item in enumerate(items):
            if pred(item):
                return i
        return -1


def get_find_first() -> FindFirst:
    return FindFirst()
