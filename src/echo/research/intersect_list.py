"""交集工具"""

from typing import List, Any, Optional


class IntersectList:
    _instance: Optional["IntersectList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def intersection(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        set2 = set(list2)
        return [item for item in list1 if item in set2]

    def intersection_by(self, list1: List[Any], list2: List[Any], key: Any) -> List[Any]:
        keys = set(key(item) for item in list2)
        return [item for item in list1 if key(item) in keys]


def get_intersect_list() -> IntersectList:
    return IntersectList()
