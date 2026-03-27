"""追加工具"""

from typing import List, Any, Optional


class AppendList:
    _instance: Optional["AppendList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def append(self, items: List[Any], item: Any) -> List[Any]:
        return items + [item]

    def append_all(self, items: List[Any], append_items: List[Any]) -> List[Any]:
        return items + append_items

    def conj(self, items: List[Any], item: Any) -> List[Any]:
        return items + [item]


def get_append_list() -> AppendList:
    return AppendList()
