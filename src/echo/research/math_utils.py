"""数学工具"""

import math
from typing import Optional


class MathUtils:
    """数学工具"""

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        """限制在范围内"""
        return max(min_val, min(max_val, value))

    def lerp(self, a: float, b: float, t: float) -> float:
        """线性插值"""
        return a + (b - a) * t

    def map_range(self, value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        """范围映射"""
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def gcd(self, a: int, b: int) -> int:
        """最大公约数"""
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a: int, b: int) -> int:
        """最小公倍数"""
        return abs(a * b) // self.gcd(a, b)

    def round_to(self, value: float, precision: int) -> float:
        """四舍五入到指定精度"""
        multiplier = 10 ** precision
        return math.round(value * multiplier) / multiplier


_utils: Optional[MathUtils] = None


def get_math_utils() -> MathUtils:
    global _utils
    if _utils is None:
        _utils = MathUtils()
    return _utils