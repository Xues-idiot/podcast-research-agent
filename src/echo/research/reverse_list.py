"""反转工具"""

from typing import List, Any, Optional


class ReverseList:
    _instance: Optional["ReverseList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, items: List[Any]) -> List[Any]:
        return items[::-1]

    def reverse_inplace(self, items: List[Any]) -> None:
        items.reverse()


def get_reverse_list() -> ReverseList:
    return ReverseList()
