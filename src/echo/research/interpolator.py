"""插值工具"""

from typing import Optional


class Interpolator:
    """插值工具"""

    def lerp(self, a: float, b: float, t: float) -> float:
        """线性插值"""
        return a + (b - a) * t

    def inverse_lerp(self, a: float, b: float, v: float) -> float:
        """逆线性插值"""
        if b == a:
            return 0
        return (v - a) / (b - a)


_tool: Optional[Interpolator] = None


def get_interpolator() -> Interpolator:
    global _tool
    if _tool is None:
        _tool = Interpolator()
    return _tool