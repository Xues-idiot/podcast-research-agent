"""积分工具"""

from typing import List, Optional


class IntegralTool:
    _instance: Optional["IntegralTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trapezoidal(self, points: List[float], dt: float = 1.0) -> float:
        if len(points) < 2:
            return 0.0
        return sum((points[i] + points[i+1]) / 2 * dt for i in range(len(points) - 1))


def get_integral_tool() -> IntegralTool:
    return IntegralTool()
