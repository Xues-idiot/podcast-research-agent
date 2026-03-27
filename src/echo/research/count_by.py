"""计数工具"""

from typing import List, Any, Callable, Dict


class CountBy:
    _instance: Optional["CountBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def count_by(self, items: List[Any], key_func: Callable = None) -> Dict[Any, int]:
        counts: Dict[Any, int] = {}
        for item in items:
            key = key_func(item) if key_func else item
            counts[key] = counts.get(key, 0) + 1
        return counts


def get_count_by() -> CountBy:
    return CountBy()
