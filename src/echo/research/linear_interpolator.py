"""线性插值器"""

from typing import List, Optional


class LinearInterpolator:
    _instance: Optional["LinearInterpolator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear_points(self, points: List[float], index: float) -> Optional[float]:
        if len(points) < 2:
            return None
        idx = int(index)
        if idx < 0 or idx >= len(points) - 1:
            return None
        t = index - idx
        return points[idx] + (points[idx + 1] - points[idx]) * t


def get_linear_interpolator() -> LinearInterpolator:
    return LinearInterpolator()
