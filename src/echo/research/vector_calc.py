"""向量计算器"""

import math
from typing import List, Optional


class VectorCalc:
    _instance: Optional["VectorCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def magnitude(self, vector: List[float]) -> float:
        return math.sqrt(sum(x ** 2 for x in vector))

    def dot_product(self, v1: List[float], v2: List[float]) -> float:
        return sum(a * b for a, b in zip(v1, v2))

    def normalize(self, vector: List[float]) -> List[float]:
        mag = self.magnitude(vector)
        if mag == 0:
            return vector
        return [x / mag for x in vector]


def get_vector_calc() -> VectorCalc:
    return VectorCalc()
