"""向量加法工具"""

from typing import List, Optional


class VectorAddTool:
    _instance: Optional["VectorAddTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a: List[float], b: List[float]) -> List[float]:
        return [a[i] + b[i] for i in range(min(len(a), len(b)))]


def get_vector_add_tool() -> VectorAddTool:
    return VectorAddTool()
