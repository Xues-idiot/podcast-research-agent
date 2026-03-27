"""求和计算器"""

from typing import List, Optional


class SumCalc:
    _instance: Optional["SumCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sum(self, values: List[float]) -> float:
        return sum(values)

    def cumulative_sum(self, values: List[float]) -> List[float]:
        result = []
        total = 0.0
        for v in values:
            total += v
            result.append(total)
        return result


def get_sum_calc() -> SumCalc:
    return SumCalc()
