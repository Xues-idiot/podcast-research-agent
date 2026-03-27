"""求和工具"""

from typing import List, Any, Optional, Callable


class SumList:
    _instance: Optional["SumList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sum(self, items: List[int]) -> int:
        return sum(items)

    def sum_by(self, items: List[Any], key: Callable) -> Any:
        return sum(key(item) for item in items)

    def product(self, items: List[int]) -> int:
        result = 1
        for item in items:
            result *= item
        return result


def get_sum_list() -> SumList:
    return SumList()
