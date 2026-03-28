"""矩阵迹工具"""

from typing import List, Optional


class MatrixTraceTool:
    _instance: Optional["MatrixTraceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trace(self, matrix: List[List[float]]) -> float:
        n = min(len(matrix), len(matrix[0]) if matrix else 0)
        return sum(matrix[i][i] for i in range(n))


def get_matrix_trace_tool() -> MatrixTraceTool:
    return MatrixTraceTool()