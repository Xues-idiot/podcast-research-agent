"""线性插值计算器"""

from typing import Optional, Tuple


class LinearInterp:
    _instance: Optional["LinearInterp"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def lerp(self, a: float, b: float, t: float) -> float:
        return a + (b - a) * t

    def inverse_lerp(self, a: float, b: float, value: float) -> float:
        if b == a:
            return 0.0
        return (value - a) / (b - a)


def get_linear_interp() -> LinearInterp:
    return LinearInterp()
