"""体积计算器"""

from typing import Optional


class VolumeCalc:
    _instance: Optional["VolumeCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cube(self, side: float) -> float:
        return side ** 3

    def sphere(self, radius: float) -> float:
        import math
        return (4/3) * math.pi * radius ** 3

    def cylinder(self, radius: float, height: float) -> float:
        import math
        return math.pi * radius ** 2 * height


def get_volume_calc() -> VolumeCalc:
    return VolumeCalc()
