"""跳过元素工具"""

from typing import List, Any, Callable, Optional


class DropWhile:
    _instance: Optional["DropWhile"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def drop_while(self, items: List[Any], pred: Callable) -> List[Any]:
        result = []
        dropping = True
        for item in items:
            if dropping and pred(item):
                continue
            dropping = False
            result.append(item)
        return result

    def drop(self, items: List[Any], n: int) -> List[Any]:
        return items[n:] if n < len(items) else []


def get_drop_while() -> DropWhile:
    return DropWhile()
