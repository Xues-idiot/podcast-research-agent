"""向量点积工具"""

from typing import List, Optional


class VectorDotTool:
    _instance: Optional["VectorDotTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def dot(self, a: List[float], b: List[float]) -> float:
        return sum(x * y for x, y in zip(a, b))


def get_vector_dot_tool() -> VectorDotTool:
    return VectorDotTool()
