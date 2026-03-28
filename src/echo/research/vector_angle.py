"""向量角度工具"""

import math
from typing import List, Optional


class VectorAngleTool:
    _instance: Optional["VectorAngleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def angle(self, a: List[float], b: List[float]) -> float:
        if len(a) != len(b) or not a or not b:
            return 0.0
        dot = sum(a[i] * b[i] for i in range(len(a)))
        mag_a = math.sqrt(sum(x * x for x in a))
        mag_b = math.sqrt(sum(x * x for x in b))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        cos_angle = max(-1.0, min(1.0, dot / (mag_a * mag_b)))
        return math.acos(cos_angle)


def get_vector_angle_tool() -> VectorAngleTool:
    return VectorAngleTool()