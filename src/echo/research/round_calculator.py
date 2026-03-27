"""四舍五入计算器"""

from typing import Optional


class RoundCalculator:
    _instance: Optional["RoundCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def round_val(self, n: float, decimals: int = 0) -> float:
        return round(n, decimals)

    def floor(self, n: float) -> int:
        return int(n // 1)

    def ceil(self, n: float) -> int:
        import math
        return math.ceil(n)

    def truncate(self, n: float) -> int:
        import math
        return math.trunc(n)


def get_round_calculator() -> RoundCalculator:
    return RoundCalculator()
