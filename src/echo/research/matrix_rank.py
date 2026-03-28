"""矩阵秩工具"""

from typing import List, Optional


class MatrixRankTool:
    _instance: Optional["MatrixRankTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rank(self, matrix: List[List[float]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        mat = [row[:] for row in matrix]
        rank = 0
        for r in range(rows):
            if rank >= rows:
                break
            if abs(mat[r][r]) < 1e-10:
                for i in range(r + 1, rows):
                    if abs(mat[i][r]) > 1e-10:
                        mat[r], mat[i] = mat[i], mat[r]
                        break
            if abs(mat[r][r]) < 1e-10:
                continue
            for i in range(r + 1, rows):
                factor = mat[i][r] / mat[r][r]
                for j in range(r, cols):
                    mat[i][j] -= factor * mat[r][j]
            rank += 1
        return rank


def get_matrix_rank_tool() -> MatrixRankTool:
    return MatrixRankTool()