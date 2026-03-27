"""插入工具"""

from typing import List, Any, Optional


class InsertList:
    _instance: Optional["InsertList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def insert(self, items: List[Any], index: int, item: Any) -> List[Any]:
        if index < 0:
            index = 0
        if index >= len(items):
            return items + [item]
        return items[:index] + [item] + items[index:]

    def insert_all(self, items: List[Any], index: int, insert_items: List[Any]) -> List[Any]:
        if index < 0:
            index = 0
        if index >= len(items):
            return items + insert_items
        return items[:index] + insert_items + items[index:]


def get_insert_list() -> InsertList:
    return InsertList()
