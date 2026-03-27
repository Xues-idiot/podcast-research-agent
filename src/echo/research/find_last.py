"""查找最后一个工具"""

from typing import List, Any, Callable, Optional


class FindLast:
    _instance: Optional["FindLast"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_last(self, items: List[Any], pred: Callable) -> Any:
        result = None
        for item in items:
            if pred(item):
                result = item
        return result

    def find_last_index(self, items: List[Any], pred: Callable) -> int:
        result = -1
        for i, item in enumerate(items):
            if pred(item):
                result = i
        return result


def get_find_last() -> FindLast:
    return FindLast()
