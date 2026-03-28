"""点是否在多边形内工具"""

from typing import List, Optional


class PointInPolygonTool:
    _instance: Optional["PointInPolygonTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def contains(self, point: List[float], vertices: List[List[float]]) -> bool:
        x, y = point
        n = len(vertices)
        inside = False
        for i in range(n):
            j = (i + 1) % n
            xi, yi = vertices[i]
            xj, yj = vertices[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
        return inside


def get_point_in_polygon_tool() -> PointInPolygonTool:
    return PointInPolygonTool()