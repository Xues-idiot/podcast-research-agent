"""合并工具"""

from typing import List, Any, Callable, Optional


class MergeList:
    _instance: Optional["MergeList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def merge(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        return list1 + list2

    def merge_by(self, list1: List[Any], list2: List[Any], key: Callable) -> List[Any]:
        merged = list1 + list2
        return sorted(merged, key=key)


def get_merge_list() -> MergeList:
    return MergeList()
