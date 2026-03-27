"""压缩列表工具"""

from typing import List, Any


class CompactList:
    _instance: Optional["CompactList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compact(self, items: List[Any]) -> List[Any]:
        return [item for item in items if item]


def get_compact_list() -> CompactList:
    return CompactList()
