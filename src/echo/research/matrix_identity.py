"""单位矩阵工具"""

from typing import List, Optional


class MatrixIdentityTool:
    _instance: Optional["MatrixIdentityTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def identity(self, size: int) -> List[List[float]]:
        return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]


def get_matrix_identity_tool() -> MatrixIdentityTool:
    return MatrixIdentityTool()
