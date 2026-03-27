"""导数计算器"""

from typing import List, Optional


class DerivativeCalc:
    _instance: Optional["DerivativeCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def derivative(self, data: List[float]) -> List[float]:
        if len(data) < 2:
            return []
        return [data[i + 1] - data[i] for i in range(len(data) - 1)]

    def second_derivative(self, data: List[float]) -> List[float]:
        if len(data) < 3:
            return []
        return [data[i + 2] - 2 * data[i + 1] + data[i] for i in range(len(data) - 2)]


def get_derivative_calc() -> DerivativeCalc:
    return DerivativeCalc()
