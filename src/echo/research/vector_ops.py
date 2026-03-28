"""向量运算工具"""

import math
from typing import List, Optional


class VectorOps:
    _instance: Optional["VectorOps"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def dot(self, a: List[float], b: List[float]) -> float:
        return sum(x * y for x, y in zip(a, b))

    def cross(self, a: List[float], b: List[float]) -> List[float]:
        return [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        ]

    def magnitude(self, v: List[float]) -> float:
        return math.sqrt(sum(x ** 2 for x in v))


def get_vector_ops() -> VectorOps:
    return VectorOps()
