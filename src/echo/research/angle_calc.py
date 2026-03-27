"""角度计算器"""

import math
from typing import Optional


class AngleCalc:
    _instance: Optional["AngleCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def degrees_to_radians(self, degrees: float) -> float:
        return degrees * math.pi / 180

    def radians_to_degrees(self, radians: float) -> float:
        return radians * 180 / math.pi

    def sin(self, angle: float) -> float:
        return math.sin(math.radians(angle))

    def cos(self, angle: float) -> float:
        return math.cos(math.radians(angle))

    def tan(self, angle: float) -> float:
        return math.tan(math.radians(angle))


def get_angle_calc() -> AngleCalc:
    return AngleCalc()
