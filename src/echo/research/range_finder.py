"""范围查找器"""

from typing import Any, List, Optional, Tuple


class RangeFinder:
    _instance: Optional["RangeFinder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def range(self, items: List[float]) -> Optional[float]:
        if len(items) < 2:
            return None
        return max(items) - min(items)

    def min_max(self, items: List[float]) -> Optional[Tuple[float, float]]:
        if not items:
            return None
        return (min(items), max(items))


def get_range_finder() -> RangeFinder:
    return RangeFinder()
