"""旋转矩阵工具"""

from typing import List, Optional


class RotateMatrixTool:
    _instance: Optional["RotateMatrixTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rotate_90(self, matrix: List[List[float]]) -> List[List[float]]:
        if not matrix:
            return []
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]) - 1, -1, -1)]


def get_rotate_matrix_tool() -> RotateMatrixTool:
    return RotateMatrixTool()
