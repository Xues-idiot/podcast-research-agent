"""Catmull-Rom样条工具"""

from typing import List, Optional


class CatmullRomSpline:
    _instance: Optional["CatmullRomSpline"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def point_at(self, points: List[List[float]], t: float) -> List[float]:
        n = len(points)
        if n < 4:
            return points[0] if points else []
        segment = min(max(int(t), 0), n - 2)
        local_t = t - segment
        p0, p1, p2, p3 = points[segment], points[segment + 1], points[segment + 2], points[min(segment + 3, n - 1)]
        t2 = local_t * local_t
        t3 = t2 * local_t
        result = []
        for i in range(len(p1)):
            result.append(0.5 * ((2 * p1[i]) + (-p0[i] + p2[i]) * local_t + (2 * p0[i] - 5 * p1[i] + 4 * p2[i] - p3[i]) * t2 + (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t3))
        return result


def get_catmull_rom_spline() -> CatmullRomSpline:
    return CatmullRomSpline()
