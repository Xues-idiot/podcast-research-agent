"""圆周计算器"""

from typing import Optional


class CircumferenceCalc:
    _instance: Optional["CircumferenceCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def circumference(self, radius: float) -> float:
        import math
        return 2 * math.pi * radius

    def arc_length(self, radius: float, angle: float) -> float:
        import math
        return radius * math.radians(angle)


def get_circumference_calc() -> CircumferenceCalc:
    return CircumferenceCalc()
