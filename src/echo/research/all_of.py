"""全部匹配工具"""

from typing import List, Any, Callable, Optional


class AllOf:
    _instance: Optional["AllOf"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def all_of(self, items: List[Any], pred: Callable = None) -> bool:
        if pred is None:
            return all(items)
        return all(pred(item) for item in items)


def get_all_of() -> AllOf:
    return AllOf()
