"""映射值工具"""

from typing import List, Any, Callable, Optional


class MapValues:
    _instance: Optional["MapValues"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def map_values(self, items: List[Any], func: Callable) -> List[Any]:
        return [func(item) for item in items]


def get_map_values() -> MapValues:
    return MapValues()
