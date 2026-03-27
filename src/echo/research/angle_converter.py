"""角度转换器"""

import math
from typing import Optional


class AngleConverter:
    _instance: Optional["AngleConverter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def degrees_to_radians(self, degrees: float) -> float:
        return degrees * math.pi / 180

    def radians_to_degrees(self, radians: float) -> float:
        return radians * 180 / math.pi

    def sin(self, degrees: float) -> float:
        return math.sin(math.radians(degrees))

    def cos(self, degrees: float) -> float:
        return math.cos(math.radians(degrees))

    def tan(self, degrees: float) -> float:
        return math.tan(math.radians(degrees))


def get_angle_converter() -> AngleConverter:
    return AngleConverter()
