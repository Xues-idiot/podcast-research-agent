"""转置工具"""

from typing import List, Any, Optional


class TransposeTool:
    _instance: Optional["TransposeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transpose(self, matrix: List[List[Any]]) -> List[List[Any]]:
        if not matrix or not matrix[0]:
            return []
        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


def get_transpose_tool() -> TransposeTool:
    return TransposeTool()
