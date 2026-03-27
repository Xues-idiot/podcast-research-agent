"""样条插值工具"""

from typing import List, Optional


class SplineTool:
    _instance: Optional["SplineTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear_interpolate(self, points: List[float], x: float) -> Optional[float]:
        if len(points) < 2:
            return None
        n = len(points)
        if x <= 0:
            return points[0]
        if x >= n - 1:
            return points[-1]
        i = int(x)
        t = x - i
        return points[i] * (1 - t) + points[i + 1] * t


def get_spline_tool() -> SplineTool:
    return SplineTool()
