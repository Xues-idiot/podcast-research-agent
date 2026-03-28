"""向量缩放工具"""

from typing import List, Optional


class VectorScaleTool:
    _instance: Optional["VectorScaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scale(self, v: List[float], factor: float) -> List[float]:
        return [x * factor for x in v]


def get_vector_scale_tool() -> VectorScaleTool:
    return VectorScaleTool()
