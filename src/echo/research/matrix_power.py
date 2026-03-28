"""矩阵幂工具"""

from typing import List, Optional


class MatrixPowerTool:
    _instance: Optional["MatrixPowerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def power(self, matrix: List[List[float]], n: int) -> List[List[float]]:
        if n == 0:
            size = len(matrix)
            return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]
        if n < 0:
            return []
        result = matrix
        for _ in range(n - 1):
            result = self._multiply(result, matrix)
        return result

    def _multiply(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        rows, cols, inner = len(a), len(b[0]), len(b)
        return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def get_matrix_power_tool() -> MatrixPowerTool:
    return MatrixPowerTool()