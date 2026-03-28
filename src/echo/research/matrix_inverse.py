"""矩阵求逆工具"""

from typing import List, Optional


class MatrixInverseTool:
    _instance: Optional["MatrixInverseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def inverse(self, matrix: List[List[float]]) -> List[List[float]]:
        n = len(matrix)
        if n == 0:
            return []
        det = self._det(matrix)
        if abs(det) < 1e-10:
            return []
        adj = self._adjoint(matrix)
        return [[adj[i][j] / det for j in range(n)] for i in range(n)]

    def _det(self, matrix: List[List[float]]) -> float:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        result = 0.0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            result += ((-1) ** j) * matrix[0][j] * self._det(minor)
        return result

    def _adjoint(self, matrix: List[List[float]]) -> List[List[float]]:
        n = len(matrix)
        if n == 1:
            return [[1.0]]
        adj = []
        for i in range(n):
            row = []
            for j in range(n):
                minor = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
                cofactor = ((-1) ** (i + j)) * self._det(minor)
                row.append(cofactor)
            adj.append(row)
        return [[adj[j][i] for j in range(n)] for i in range(n)]


def get_matrix_inverse_tool() -> MatrixInverseTool:
    return MatrixInverseTool()