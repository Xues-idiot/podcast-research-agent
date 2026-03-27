"""Zip工具"""

from typing import List, Any, Callable, Optional


class ZipWith:
    _instance: Optional["ZipWith"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_with(self, list1: List[Any], list2: List[Any], func: Callable) -> List[Any]:
        min_len = min(len(list1), len(list2))
        return [func(list1[i], list2[i]) for i in range(min_len)]

    def zip_all(self, *lists: List[Any]) -> List[tuple]:
        max_len = max(len(lst) for lst in lists)
        result = []
        for i in range(max_len):
            result.append(tuple(lst[i] if i < len(lst) else None for lst in lists))
        return result


def get_zip_with() -> ZipWith:
    return ZipWith()
