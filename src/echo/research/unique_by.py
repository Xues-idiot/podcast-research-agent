"""按键去重工具"""

from typing import List, Any, Callable, Optional


class UniqueBy:
    _instance: Optional["UniqueBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def unique_by(self, items: List[Any], key: Callable) -> List[Any]:
        seen = set()
        result = []
        for item in items:
            k = key(item)
            if k not in seen:
                seen.add(k)
                result.append(item)
        return result

    def distinct(self, items: List[Any]) -> List[Any]:
        result = []
        for item in items:
            if item not in result:
                result.append(item)
        return result


def get_unique_by() -> UniqueBy:
    return UniqueBy()
