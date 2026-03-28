"""矩阵行列式工具"""

from typing import List, Optional


class MatrixDeterminantTool:
    _instance: Optional["MatrixDeterminantTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def determinant(self, matrix: List[List[float]]) -> float:
        n = len(matrix)
        if n == 0:
            return 1.0
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0.0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            cofactor = ((-1) ** j) * matrix[0][j] * self.determinant(minor)
            det += cofactor
        return det


def get_matrix_determinant_tool() -> MatrixDeterminantTool:
    return MatrixDeterminantTool()