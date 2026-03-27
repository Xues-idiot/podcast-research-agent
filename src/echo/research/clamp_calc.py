"""区间限制计算器"""

from typing import Optional


class ClampCalc:
    _instance: Optional["ClampCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        return max(min_val, min(max_val, value))

    def in_range(self, value: float, min_val: float, max_val: float) -> bool:
        return min_val <= value <= max_val


def get_clamp_calc() -> ClampCalc:
    return ClampCalc()
