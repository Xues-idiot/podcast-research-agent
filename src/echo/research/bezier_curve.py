"""贝塞尔曲线工具"""

from typing import List, Optional


class BezierCurve:
    _instance: Optional["BezierCurve"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def point_at(self, control_points: List[List[float]], t: float) -> List[float]:
        n = len(control_points)
        if n == 0:
            return []
        result = [0.0] * len(control_points[0])
        for i, point in enumerate(control_points):
            binomial = self._binomial(n - 1, i)
            factor = binomial * (t ** i) * ((1 - t) ** (n - 1 - i))
            for j, coord in enumerate(point):
                result[j] += factor * coord
        return result

    def _binomial(self, n: int, k: int) -> float:
        from math import comb
        return comb(n, k)


def get_bezier_curve() -> BezierCurve:
    return BezierCurve()
