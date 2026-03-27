"""Zip生成工具"""

from typing import List, Any, Optional


class ZipGen:
    _instance: Optional["ZipGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip(self, *lists: List[Any]) -> List[tuple]:
        return list(zip(*lists))

    def zip_longest(self, *lists: List[Any], fillvalue: Any = None) -> List[tuple]:
        max_len = max(len(lst) for lst in lists)
        result = []
        for i in range(max_len):
            result.append(tuple(
                lists[j][i] if i < len(lists[j]) else fillvalue
                for j in range(len(lists))
            ))
        return result


def get_zip_gen() -> ZipGen:
    return ZipGen()
