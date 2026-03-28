"""矩阵乘法工具"""

from typing import List, Optional


class MatrixMultiplyTool:
    _instance: Optional["MatrixMultiplyTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def multiply(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        if not a or not b or len(a[0]) != len(b):
            return []
        rows_a, cols_a = len(a), len(a[0])
        cols_b = len(b[0])
        result = [[0.0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result


def get_matrix_multiply_tool() -> MatrixMultiplyTool:
    return MatrixMultiplyTool()
