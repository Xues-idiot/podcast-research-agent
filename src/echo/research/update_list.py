"""更新工具"""

from typing import List, Any, Callable, Optional


class UpdateList:
    _instance: Optional["UpdateList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def update(self, items: List[Any], index: int, item: Any) -> List[Any]:
        if 0 <= index < len(items):
            result = items.copy()
            result[index] = item
            return result
        return items

    def update_where(self, items: List[Any], pred: Callable, item: Any) -> List[Any]:
        return [item if pred(i, x) else x for i, x in enumerate(items)]

    def replace(self, items: List[Any], old: Any, new: Any) -> List[Any]:
        return [new if x == old else x for x in items]


def get_update_list() -> UpdateList:
    return UpdateList()
