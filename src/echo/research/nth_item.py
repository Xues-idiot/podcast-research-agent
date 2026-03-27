"""第N个元素工具"""

from typing import List, Any, Optional


class NthItem:
    _instance: Optional["NthItem"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def nth(self, items: List[Any], n: int, default: Any = None) -> Any:
        if n < 0:
            n = len(items) + n
        return items[n] if 0 <= n < len(items) else default

    def second(self, items: List[Any]) -> Any:
        return self.nth(items, 1)

    def third(self, items: List[Any]) -> Any:
        return self.nth(items, 2)


def get_nth_item() -> NthItem:
    return NthItem()
