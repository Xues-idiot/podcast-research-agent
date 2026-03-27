"""循环生成工具"""

from typing import List, Any, Iterator, Optional
import itertools


class CycleGen:
    _instance: Optional["CycleGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cycle(self, items: List[Any], count: int) -> List[Any]:
        result = []
        for _ in range(count):
            result.extend(items)
        return result

    def infinite_cycle(self, items: List[Any]) -> Iterator:
        return itertools.cycle(items)


def get_cycle_gen() -> CycleGen:
    return CycleGen()
