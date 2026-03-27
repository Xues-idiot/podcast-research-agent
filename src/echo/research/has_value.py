"""存在检查工具"""

from typing import List, Any, Callable, Optional


class HasValue:
    _instance: Optional["HasValue"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def has(self, items: List[Any], value: Any) -> bool:
        return value in items

    def has_pred(self, items: List[Any], pred: Callable) -> bool:
        return any(pred(item) for item in items)


def get_has_value() -> HasValue:
    return HasValue()
