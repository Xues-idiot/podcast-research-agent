"""B样条曲线工具"""

from typing import List, Optional


class BSpline:
    _instance: Optional["BSpline"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def point_at(self, control_points: List[List[float]], t: float, degree: int = 3) -> List[float]:
        n = len(control_points) - 1
        if n < degree:
            return control_points[0] if control_points else []
        result = [0.0] * len(control_points[0])
        for i, point in enumerate(control_points):
            basis = self._basis(i, degree, t, n + 1)
            for j, coord in enumerate(point):
                result[j] += basis * coord
        return result

    def _basis(self, i: int, k: int, t: float, n: int) -> float:
        if k == 0:
            return 1.0 if i <= t < i + 1 else 0.0
        d1 = self._basis(i, k - 1, t, n)
        d2 = self._basis(i + 1, k - 1, t, n)
        denom1 = i + k - t if i + k - t != 0 else 1
        denom2 = i + 1 + k - t if i + 1 + k - t != 0 else 1
        return d1 * (t - i) / denom1 + d2 * (i + k + 1 - t) / denom2


def get_bspline() -> BSpline:
    return BSpline()
