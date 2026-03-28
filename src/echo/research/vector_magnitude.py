"""向量模长工具"""

import math
from typing import List, Optional


class VectorMagnitudeTool:
    _instance: Optional["VectorMagnitudeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def magnitude(self, v: List[float]) -> float:
        if not v:
            return 0.0
        return math.sqrt(sum(x * x for x in v))


def get_vector_magnitude_tool() -> VectorMagnitudeTool:
    return VectorMagnitudeTool()