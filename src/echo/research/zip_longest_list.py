"""Zip最长工具"""

from typing import List, Any, Optional, Callable


class ZipLongest:
    _instance: Optional["ZipLongest"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_longest(self, *lists: List[Any], fillvalue: Any = None) -> List[tuple]:
        max_len = max(len(lst) for lst in lists)
        result = []
        for i in range(max_len):
            result.append(tuple(
                lists[j][i] if i < len(lists[j]) else fillvalue
                for j in range(len(lists))
            ))
        return result

    def zip_longest_with(self, list1: List[Any], list2: List[Any], func: Callable, fillvalue: Any = None) -> List[Any]:
        max_len = max(len(list1), len(list2))
        result = []
        for i in range(max_len):
            a = list1[i] if i < len(list1) else fillvalue
            b = list2[i] if i < len(list2) else fillvalue
            result.append(func(a, b))
        return result


def get_zip_longest() -> ZipLongest:
    return ZipLongest()
