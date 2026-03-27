"""每个元素检查"""

from typing import List, Any, Callable, Optional


class EveryItem:
    _instance: Optional["EveryItem"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def every(self, items: List[Any], pred: Callable = None) -> bool:
        if pred is None:
            return all(items)
        return all(pred(item) for item in items)


def get_every_item() -> EveryItem:
    return EveryItem()
