"""向量钳制工具"""

from typing import List, Optional


class VectorClampTool:
    _instance: Optional["VectorClampTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clamp(self, v: List[float], min_val: float, max_val: float) -> List[float]:
        if min_val > max_val:
            min_val, max_val = max_val, min_val
        return [max(min_val, min(max_val, x)) for x in v]


def get_vector_clamp_tool() -> VectorClampTool:
    return VectorClampTool()