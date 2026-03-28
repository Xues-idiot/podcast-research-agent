"""向量归一化工具"""

import math
from typing import List, Optional


class VectorNormalizeTool:
    _instance: Optional["VectorNormalizeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, v: List[float]) -> List[float]:
        if not v:
            return v
        mag = math.sqrt(sum(x * x for x in v))
        if mag == 0:
            return v
        return [x / mag for x in v]


def get_vector_normalize_tool() -> VectorNormalizeTool:
    return VectorNormalizeTool()
