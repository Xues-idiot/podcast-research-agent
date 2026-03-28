"""求和与乘积工具"""

from typing import List, Optional


class SumProductTool:
    _instance: Optional["SumProductTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sum(self, numbers: List[float]) -> float:
        return sum(numbers)

    def product(self, numbers: List[float]) -> float:
        result = 1.0
        for n in numbers:
            result *= n
        return result

    def average(self, numbers: List[float]) -> float:
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)


def get_sum_product_tool() -> SumProductTool:
    return SumProductTool()