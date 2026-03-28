"""圆面积工具"""

import math
from typing import Optional


class CircleAreaTool:
    _instance: Optional["CircleAreaTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def area(self, radius: float) -> float:
        if radius < 0:
            return 0.0
        return math.pi * radius * radius


def get_circle_area_tool() -> CircleAreaTool:
    return CircleAreaTool()