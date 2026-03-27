"""枚举工具"""

from typing import List, Any, Optional


class EnumerateList:
    _instance: Optional["EnumerateList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def enumerate(self, items: List[Any], start: int = 0) -> List[tuple]:
        return list(enumerate(items, start))

    def with_index(self, items: List[Any], start: int = 0) -> List[dict]:
        return [{"index": i, "item": item} for i, item in enumerate(items, start)]


def get_enumerate_list() -> EnumerateList:
    return EnumerateList()
