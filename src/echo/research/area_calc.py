"""面积计算器"""

from typing import Optional


class AreaCalc:
    _instance: Optional["AreaCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rectangle(self, width: float, height: float) -> float:
        return width * height

    def circle(self, radius: float) -> float:
        import math
        return math.pi * radius ** 2

    def triangle(self, base: float, height: float) -> float:
        return 0.5 * base * height


def get_area_calc() -> AreaCalc:
    return AreaCalc()
