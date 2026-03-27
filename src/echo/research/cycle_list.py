"""循环工具"""

from typing import List, Any, Iterator, Optional
import itertools


class CycleList:
    _instance: Optional["CycleList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cycle(self, items: List[Any], n: int = None) -> List[Any]:
        if n is None:
            return list(itertools.chain.from_iterable(itertools.repeat(items)))
        result = []
        for _ in range(n):
            result.extend(items)
        return result

    def infinite_cycle(self, items: List[Any]) -> Iterator:
        return itertools.cycle(items)


def get_cycle_list() -> CycleList:
    return CycleList()
