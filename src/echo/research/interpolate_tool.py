"""插值工具"""

from typing import List, Optional, Tuple


class InterpolateTool:
    _instance: Optional["InterpolateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear(self, x: float, points: List[Tuple[float, float]]) -> float:
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if x1 <= x <= x2:
                t = (x - x1) / (x2 - x1) if x2 != x1 else 0
                return y1 + t * (y2 - y1)
        return points[-1][1] if points else 0.0


def get_interpolate_tool() -> InterpolateTool:
    return InterpolateTool()
