"""查找所有工具"""

from typing import List, Any, Callable, Optional


class FindAll:
    _instance: Optional["FindAll"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_all(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if pred(item)]


def get_find_all() -> FindAll:
    return FindAll()
