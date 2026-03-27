"""条件计数工具"""

from typing import List, Any, Callable, Optional


class CountIf:
    _instance: Optional["CountIf"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def count_if(self, items: List[Any], pred: Callable) -> int:
        return sum(1 for item in items if pred(item))

    def count_by(self, items: List[Any], key: Callable) -> int:
        return sum(1 for item in items if key(item))


def get_count_if() -> CountIf:
    return CountIf()
