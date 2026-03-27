"""获取元素工具"""

from typing import List, Any, Callable, Optional


class TakeWhile:
    _instance: Optional["TakeWhile"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def take_while(self, items: List[Any], pred: Callable) -> List[Any]:
        result = []
        for item in items:
            if pred(item):
                result.append(item)
            else:
                break
        return result

    def take(self, items: List[Any], n: int) -> List[Any]:
        return items[:n]


def get_take_while() -> TakeWhile:
    return TakeWhile()
