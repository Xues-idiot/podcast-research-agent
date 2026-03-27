"""向量工具"""

import math
from typing import List, Optional


class VectorTool:
    _instance: Optional["VectorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def magnitude(self, v: List[float]) -> float:
        return math.sqrt(sum(x ** 2 for x in v))

    def normalize(self, v: List[float]) -> Optional[List[float]]:
        mag = self.magnitude(v)
        if mag == 0:
            return None
        return [x / mag for x in v]

    def dot(self, a: List[float], b: List[float]) -> Optional[float]:
        if len(a) != len(b):
            return None
        return sum(x * y for x, y in zip(a, b))


def get_vector_tool() -> VectorTool:
    return VectorTool()
