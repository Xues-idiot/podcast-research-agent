"""向量旋转工具"""

import math
from typing import List, Optional


class VectorRotateTool:
    _instance: Optional["VectorRotateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rotate_2d(self, v: List[float], angle: float) -> List[float]:
        if len(v) != 2:
            return v
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return [
            v[0] * cos_a - v[1] * sin_a,
            v[0] * sin_a + v[1] * cos_a
        ]

    def rotate_3d(self, v: List[float], axis: List[float], angle: float) -> List[float]:
        if len(v) != 3 or len(axis) != 3:
            return v
        axis = self._normalize(axis)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return [
            v[0] * cos_a + (axis[1] * v[2] - axis[2] * v[1]) * sin_a + axis[0] * (v[0] * axis[0] + v[1] * axis[1] + v[2] * axis[2]) * (1 - cos_a),
            v[1] * cos_a + (axis[2] * v[0] - axis[0] * v[2]) * sin_a + axis[1] * (v[0] * axis[0] + v[1] * axis[1] + v[2] * axis[2]) * (1 - cos_a),
            v[2] * cos_a + (axis[0] * v[1] - axis[1] * v[0]) * sin_a + axis[2] * (v[0] * axis[0] + v[1] * axis[1] + v[2] * axis[2]) * (1 - cos_a)
        ]

    def _normalize(self, v: List[float]) -> List[float]:
        mag = math.sqrt(sum(x * x for x in v))
        if mag == 0:
            return v
        return [x / mag for x in v]


def get_vector_rotate_tool() -> VectorRotateTool:
    return VectorRotateTool()