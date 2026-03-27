"""删除工具"""

from typing import List, Any, Callable, Optional


class DeleteList:
    _instance: Optional["DeleteList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def delete(self, items: List[Any], index: int) -> List[Any]:
        if 0 <= index < len(items):
            return items[:index] + items[index + 1:]
        return items

    def delete_where(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for i, item in enumerate(items) if not pred(i, item)]

    def remove(self, items: List[Any], item: Any) -> List[Any]:
        return [x for x in items if x != item]


def get_delete_list() -> DeleteList:
    return DeleteList()
