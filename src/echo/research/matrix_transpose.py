"""矩阵转置工具"""

from typing import List, Optional


class MatrixTransposeTool:
    _instance: Optional["MatrixTransposeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transpose(self, matrix: List[List[float]]) -> List[List[float]]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def get_matrix_transpose_tool() -> MatrixTransposeTool:
    return MatrixTransposeTool()