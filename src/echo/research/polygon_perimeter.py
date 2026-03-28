"""多边形周长工具"""

import math
from typing import List, Optional


class PolygonPerimeterTool:
    _instance: Optional["PolygonPerimeterTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def perimeter(self, vertices: List[List[float]]) -> float:
        if len(vertices) < 2:
            return 0.0
        n = len(vertices)
        total = 0.0
        for i in range(n):
            j = (i + 1) % n
            dx = vertices[j][0] - vertices[i][0]
            dy = vertices[j][1] - vertices[i][1]
            total += math.sqrt(dx * dx + dy * dy)
        return total


def get_polygon_perimeter_tool() -> PolygonPerimeterTool:
    return PolygonPerimeterTool()