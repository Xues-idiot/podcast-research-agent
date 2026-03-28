"""向量叉积工具"""

from typing import List, Optional


class VectorCrossTool:
    _instance: Optional["VectorCrossTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cross(self, a: List[float], b: List[float]) -> List[float]:
        if len(a) != 3 or len(b) != 3:
            return []
        return [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        ]


def get_vector_cross_tool() -> VectorCrossTool:
    return VectorCrossTool()
