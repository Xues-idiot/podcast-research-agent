"""矩阵加法工具"""

from typing import List, Optional


class MatrixAddTool:
    _instance: Optional["MatrixAddTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        if not a or not b or len(a) != len(b) or len(a[0]) != len(b[0]):
            return []
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def get_matrix_add_tool() -> MatrixAddTool:
    return MatrixAddTool()
