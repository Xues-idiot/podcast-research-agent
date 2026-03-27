"""选择工具"""

from typing import List, Any, Callable, Optional


class SelectList:
    _instance: Optional["SelectList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def select(self, items: List[Any], indices: List[int]) -> List[Any]:
        return [items[i] for i in indices if 0 <= i < len(items)]

    def select_where(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if pred(item)]


def get_select_list() -> SelectList:
    return SelectList()
