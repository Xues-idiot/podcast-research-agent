"""过滤器映射器"""

from typing import Callable, List, Optional, TypeVar


T = TypeVar("T")
R = TypeVar("R")


class FilterMap:
    _instance: Optional["FilterMap"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter_map(self, items: List[T], filter_func: Callable[[T], bool], map_func: Callable[[T], R]) -> List[R]:
        return [map_func(item) for item in items if filter_func(item)]

    def flat_map(self, items: List[T], func: Callable[[T], List[R]]) -> List[R]:
        result = []
        for item in items:
            result.extend(func(item))
        return result


def get_filter_map() -> FilterMap:
    return FilterMap()
