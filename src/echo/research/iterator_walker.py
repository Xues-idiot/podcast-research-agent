"""迭代器遍历器"""

from typing import Any, Callable, Iterator, List, Optional, TypeVar


T = TypeVar("T")
R = TypeVar("R")


class IteratorWalker:
    _instance: Optional["IteratorWalker"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def walk(self, iterator: Iterator[T], func: Callable[[T], R]) -> List[R]:
        return [func(item) for item in iterator]

    def walk_while(self, iterator: Iterator[T], condition: Callable[[T], bool]) -> List[T]:
        result = []
        for item in iterator:
            if condition(item):
                result.append(item)
            else:
                break
        return result

    def walk_until(self, iterator: Iterator[T], condition: Callable[[T], bool]) -> List[T]:
        result = []
        for item in iterator:
            if not condition(item):
                result.append(item)
            else:
                break
        return result


def get_iterator_walker() -> IteratorWalker:
    return IteratorWalker()
