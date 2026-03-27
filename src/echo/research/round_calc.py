"""四舍五入计算器"""

from typing import Optional


class RoundCalc:
    _instance: Optional["RoundCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def round_val(self, value: float, decimals: int = 0) -> float:
        return round(value, decimals)

    def floor_val(self, value: float) -> float:
        import math
        return math.floor(value)

    def ceil_val(self, value: float) -> float:
        import math
        return math.ceil(value)


def get_round_calc() -> RoundCalc:
    return RoundCalc()
