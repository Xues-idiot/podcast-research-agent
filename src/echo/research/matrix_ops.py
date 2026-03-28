"""矩阵运算工具"""

from typing import List, Optional


class MatrixOps:
    _instance: Optional["MatrixOps"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def multiply(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        rows_a, cols_a = len(a), len(a[0]) if a else 0
        rows_b, cols_b = len(b), len(b[0]) if b else 0
        if cols_a != rows_b:
            return []
        result = [[0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def transpose(self, m: List[List[float]]) -> List[List[float]]:
        if not m:
            return []
        return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def get_matrix_ops() -> MatrixOps:
    return MatrixOps()
