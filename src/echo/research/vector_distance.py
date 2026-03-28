"""向量距离工具"""

import math
from typing import List, Optional


class VectorDistanceTool:
    _instance: Optional["VectorDistanceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def distance(self, a: List[float], b: List[float]) -> float:
        if len(a) != len(b):
            return 0.0
        squared = sum((a[i] - b[i]) ** 2 for i in range(len(a)))
        return math.sqrt(squared)


def get_vector_distance_tool() -> VectorDistanceTool:
    return VectorDistanceTool()