"""导数工具"""

from typing import List, Optional


class DerivativeTool:
    _instance: Optional["DerivativeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def derivative(self, points: List[float], dt: float = 1.0) -> List[float]:
        if len(points) < 2:
            return []
        return [(points[i+1] - points[i]) / dt for i in range(len(points) - 1)]


def get_derivative_tool() -> DerivativeTool:
    return DerivativeTool()
