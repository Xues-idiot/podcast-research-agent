"""向量减法工具"""

from typing import List, Optional


class VectorSubtractTool:
    _instance: Optional["VectorSubtractTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def subtract(self, a: List[float], b: List[float]) -> List[float]:
        return [a[i] - b[i] for i in range(min(len(a), len(b)))]


def get_vector_subtract_tool() -> VectorSubtractTool:
    return VectorSubtractTool()
