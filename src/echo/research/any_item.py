"""任意元素检查"""

from typing import List, Any, Callable, Optional


class AnyItem:
    _instance: Optional["AnyItem"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def any(self, items: List[Any], pred: Callable = None) -> bool:
        if pred is None:
            return any(items)
        return any(pred(item) for item in items)


def get_any_item() -> AnyItem:
    return AnyItem()
