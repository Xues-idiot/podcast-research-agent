"""过滤工具"""

from typing import List, Any, Callable


class FilterBy:
    _instance: Optional["FilterBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter_by(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if pred(item)]


def get_filter_by() -> FilterBy:
    return FilterBy()
