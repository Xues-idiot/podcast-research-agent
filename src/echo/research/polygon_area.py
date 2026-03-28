"""多边形面积工具"""

from typing import List, Optional


class PolygonAreaTool:
    _instance: Optional["PolygonAreaTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def area(self, vertices: List[List[float]]) -> float:
        if len(vertices) < 3:
            return 0.0
        n = len(vertices)
        total = 0.0
        for i in range(n):
            j = (i + 1) % n
            total += vertices[i][0] * vertices[j][1]
            total -= vertices[j][0] * vertices[i][1]
        return abs(total) / 2.0


def get_polygon_area_tool() -> PolygonAreaTool:
    return PolygonAreaTool()