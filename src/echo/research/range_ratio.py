"""极差比计算器"""

from typing import List, Optional


class RangeRatio:
    _instance: Optional["RangeRatio"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def range_ratio(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        max_val = max(data)
        min_val = min(data)
        if min_val == 0:
            return None
        return max_val / min_val


def get_range_ratio() -> RangeRatio:
    return RangeRatio()
