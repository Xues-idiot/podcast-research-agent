"""乘积计算器"""

from functools import reduce
from typing import List, Optional


class ProductCalc:
    _instance: Optional["ProductCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def product(self, values: List[float]) -> float:
        return reduce(lambda a, b: a * b, values, 1.0)

    def cumulative_product(self, values: List[float]) -> List[float]:
        result = []
        total = 1.0
        for v in values:
            total *= v
            result.append(total)
        return result


def get_product_calc() -> ProductCalc:
    return ProductCalc()
