"""无元素检查"""

from typing import List, Any, Callable, Optional


class NoItem:
    _instance: Optional["NoItem"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def none(self, items: List[Any], pred: Callable = None) -> bool:
        if pred is None:
            return not any(items)
        return not any(pred(item) for item in items)


def get_no_item() -> NoItem:
    return NoItem()
