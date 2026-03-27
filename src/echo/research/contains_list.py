"""包含检查工具"""

from typing import List, Any, Callable, Optional


class ContainsList:
    _instance: Optional["ContainsList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def contains(self, items: List[Any], item: Any) -> bool:
        return item in items

    def contains_any(self, items: List[Any], targets: List[Any]) -> bool:
        return any(item in targets for item in items)

    def contains_all(self, items: List[Any], targets: List[Any]) -> bool:
        return all(item in targets for item in items)

    def contains_pred(self, items: List[Any], pred: Callable) -> bool:
        return any(pred(item) for item in items)


def get_contains_list() -> ContainsList:
    return ContainsList()
