"""首尾元素工具"""

from typing import List, Any, Optional


class FirstLast:
    _instance: Optional["FirstLast"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def first(self, items: List[Any]) -> Any:
        return items[0] if items else None

    def last(self, items: List[Any]) -> Any:
        return items[-1] if items else None

    def rest(self, items: List[Any]) -> List[Any]:
        return items[1:] if items else []

    def but_last(self, items: List[Any]) -> List[Any]:
        return items[:-1] if items else []


def get_first_last() -> FirstLast:
    return FirstLast()
