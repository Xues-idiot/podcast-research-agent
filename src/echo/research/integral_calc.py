"""积分计算器"""

from typing import List, Optional


class IntegralCalc:
    _instance: Optional["IntegralCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def integrate(self, data: List[float], dx: float = 1.0) -> List[float]:
        result = [0.0]
        for i in range(len(data)):
            result.append(result[-1] + data[i] * dx)
        return result[1:]

    def trapezoid(self, data: List[float], dx: float = 1.0) -> float:
        if len(data) < 2:
            return 0.0
        return dx * (sum(data) - (data[0] + data[-1]) / 2)


def get_integral_calc() -> IntegralCalc:
    return IntegralCalc()
