"""范围计算器"""

from typing import List, Optional


class RangeCalc:
    _instance: Optional["RangeCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def range_val(self, values: List[float]) -> float:
        if not values:
            return 0.0
        return max(values) - min(values)

    def midrange(self, values: List[float]) -> float:
        if not values:
            return 0.0
        return (max(values) + min(values)) / 2


def get_range_calc() -> RangeCalc:
    return RangeCalc()
