"""切片工具"""

from typing import List, Any, Optional


class SliceList:
    _instance: Optional["SliceList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def slice(self, items: List[Any], start: int = 0, end: int = None) -> List[Any]:
        return items[start:end]

    def head(self, items: List[Any], n: int = 1) -> List[Any]:
        return items[:n]

    def tail(self, items: List[Any], n: int = 1) -> List[Any]:
        return items[-n:] if n > 0 else items[:-n]


def get_slice_list() -> SliceList:
    return SliceList()
