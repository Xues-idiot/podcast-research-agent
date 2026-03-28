"""线段交点工具"""

from typing import List, Optional, Tuple


class LineIntersectionTool:
    _instance: Optional["LineIntersectionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def intersection(self, p1: List[float], p2: List[float], p3: List[float], p4: List[float]) -> Tuple[float, float]:
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(denom) < 1e-10:
            return (x1, y1)
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def get_line_intersection_tool() -> LineIntersectionTool:
    return LineIntersectionTool()