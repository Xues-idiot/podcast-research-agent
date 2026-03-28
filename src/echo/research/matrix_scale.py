"""矩阵缩放工具"""

from typing import List, Optional


class MatrixScaleTool:
    _instance: Optional["MatrixScaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scale(self, matrix: List[List[float]], factor: float) -> List[List[float]]:
        return [[cell * factor for cell in row] for row in matrix]


def get_matrix_scale_tool() -> MatrixScaleTool:
    return MatrixScaleTool()
