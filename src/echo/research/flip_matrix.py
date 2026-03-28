"""翻转矩阵工具"""

from typing import List, Optional


class FlipMatrixTool:
    _instance: Optional["FlipMatrixTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flip_horizontal(self, matrix: List[List[float]]) -> List[List[float]]:
        return [list(reversed(row)) for row in matrix]

    def flip_vertical(self, matrix: List[List[float]]) -> List[List[float]]:
        return list(reversed(matrix))


def get_flip_matrix_tool() -> FlipMatrixTool:
    return FlipMatrixTool()
