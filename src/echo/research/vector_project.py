"""向量投影工具"""

import math
from typing import List, Optional


class VectorProjectTool:
    _instance: Optional["VectorProjectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def project(self, a: List[float], b: List[float]) -> List[float]:
        if len(a) != len(b) or not b:
            return a
        dot_ab = sum(a[i] * b[i] for i in range(len(a)))
        dot_bb = sum(b[i] * b[i] for i in range(len(b)))
        if dot_bb == 0:
            return a
        scalar = dot_ab / dot_bb
        return [scalar * b[i] for i in range(len(b))]


def get_vector_project_tool() -> VectorProjectTool:
    return VectorProjectTool()