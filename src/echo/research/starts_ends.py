"""首尾检查工具"""

from typing import List, Any, Callable, Optional


class StartsEnds:
    _instance: Optional["StartsEnds"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def starts_with(self, items: List[Any], prefix: List[Any]) -> bool:
        return items[:len(prefix)] == prefix if len(items) >= len(prefix) else False

    def ends_with(self, items: List[Any], suffix: List[Any]) -> bool:
        return items[-len(suffix):] == suffix if len(items) >= len(suffix) else False

    def starts_with_pred(self, items: List[Any], pred: Callable) -> bool:
        return pred(items[0]) if items else False

    def ends_with_pred(self, items: List[Any], pred: Callable) -> bool:
        return pred(items[-1]) if items else False


def get_starts_ends() -> StartsEnds:
    return StartsEnds()
