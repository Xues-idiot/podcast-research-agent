"""可压缩生成器"""

from typing import Any, Iterator, List, Optional, Tuple, TypeVar


T = TypeVar("T")


class ZippableGen:
    _instance: Optional["ZippableGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_pairs(self, items: List[T]) -> List[Tuple[T, T]]:
        return [(items[i], items[i + 1]) for i in range(0, len(items) - 1, 2)]

    def pair_wise(self, items: List[T]) -> Iterator[Tuple[T, T]]:
        for i in range(len(items) - 1):
            yield (items[i], items[i + 1])


def get_zippable_gen() -> ZippableGen:
    return ZippableGen()
