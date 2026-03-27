"""差集工具"""

from typing import List, Any, Optional


class DiffList:
    _instance: Optional["DiffList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def difference(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        set2 = set(list2)
        return [item for item in list1 if item not in set2]

    def symmetric_difference(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        set1 = set(list1)
        set2 = set(list2)
        return list(set1 ^ set2)

    def diff_by(self, list1: List[Any], list2: List[Any], key: Any) -> List[Any]:
        keys = set(key(item) for item in list2)
        return [item for item in list1 if key(item) not in keys]


def get_diff_list() -> DiffList:
    return DiffList()
