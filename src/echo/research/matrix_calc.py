"""矩阵计算器"""

from typing import List, Optional


class MatrixCalc:
    _instance: Optional["MatrixCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transpose(self, matrix: List[List[float]]) -> List[List[float]]:
        return list(zip(*matrix))

    def multiply(self, m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m2[0])):
                val = sum(m1[i][k] * m2[k][j] for k in range(len(m2)))
                row.append(val)
            result.append(row)
        return result


def get_matrix_calc() -> MatrixCalc:
    return MatrixCalc()
