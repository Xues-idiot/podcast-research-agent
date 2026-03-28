"""向量反射工具"""

import math
from typing import List, Optional


class VectorReflectTool:
    _instance: Optional["VectorReflectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reflect(self, v: List[float], normal: List[float]) -> List[float]:
        if len(v) != len(normal) or not normal:
            return v
        dot_vn = sum(v[i] * normal[i] for i in range(len(v)))
        dot_nn = sum(normal[i] * normal[i] for i in range(len(normal)))
        if dot_nn == 0:
            return v
        scalar = 2.0 * dot_vn / dot_nn
        return [v[i] - scalar * normal[i] for i in range(len(v))]


def get_vector_reflect_tool() -> VectorReflectTool:
    return VectorReflectTool()