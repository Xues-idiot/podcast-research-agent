"""周长计算器"""

from typing import Optional


class PerimeterCalc:
    _instance: Optional["PerimeterCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rectangle(self, width: float, height: float) -> float:
        return 2 * (width + height)

    def circle(self, radius: float) -> float:
        import math
        return 2 * math.pi * radius

    def triangle(self, a: float, b: float, c: float) -> float:
        return a + b + c


def get_perimeter_calc() -> PerimeterCalc:
    return PerimeterCalc()
