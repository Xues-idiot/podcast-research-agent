"""Hermite样条工具"""

from typing import List, Optional


class HermiteSpline:
    _instance: Optional["HermiteSpline"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interpolate(self, p0: List[float], p1: List[float], m0: List[float], m1: List[float], t: float) -> List[float]:
        t2 = t * t
        t3 = t2 * t
        h00 = 2 * t3 - 3 * t2 + 1
        h10 = t3 - 2 * t2 + t
        h01 = -2 * t3 + 3 * t2
        h11 = t3 - t2
        result = []
        for i in range(len(p0)):
            result.append(h00 * p0[i] + h10 * m0[i] + h01 * p1[i] + h11 * m1[i])
        return result


def get_hermite_spline() -> HermiteSpline:
    return HermiteSpline()
