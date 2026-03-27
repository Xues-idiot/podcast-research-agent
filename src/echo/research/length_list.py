"""长度工具"""

from typing import List, Any, Optional


class LengthList:
    _instance: Optional["LengthList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def length(self, items: List[Any]) -> int:
        return len(items)

    def is_empty(self, items: List[Any]) -> bool:
        return len(items) == 0

    def is_not_empty(self, items: List[Any]) -> bool:
        return len(items) > 0


def get_length_list() -> LengthList:
    return LengthList()
