"""索引查找工具"""

from typing import List, Any, Callable, Optional


class IndexOf:
    _instance: Optional["IndexOf"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def index_of(self, items: List[Any], item: Any) -> int:
        for i, x in enumerate(items):
            if x == item:
                return i
        return -1

    def last_index_of(self, items: List[Any], item: Any) -> int:
        result = -1
        for i, x in enumerate(items):
            if x == item:
                result = i
        return result

    def find_index(self, items: List[Any], pred: Callable) -> int:
        for i, item in enumerate(items):
            if pred(item):
                return i
        return -1


def get_index_of() -> IndexOf:
    return IndexOf()
