"""矩阵工具"""

from typing import List, Optional


class MatrixTool:
    _instance: Optional["MatrixTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transpose(self, matrix: List[List[float]]) -> List[List[float]]:
        if not matrix or not matrix[0]:
            return []
        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

    def add(self, a: List[List[float]], b: List[List[float]]) -> Optional[List[List[float]]]:
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            return None
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def get_matrix_tool() -> MatrixTool:
    return MatrixTool()
