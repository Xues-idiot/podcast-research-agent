"""唯一迭代器"""

from typing import Iterator, Any, Set, Optional


class UniqueIterator:
    _instance: Optional["UniqueIterator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def unique(self, items: Iterator) -> Iterator[Any]:
        seen: Set[Any] = set()
        for item in items:
            if item not in seen:
                seen.add(item)
                yield item


def get_unique_iterator() -> UniqueIterator:
    return UniqueIterator()
