"""数独工具"""

from typing import List, Optional


class Sudoku:
    _instance: Optional["Sudoku"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def solve(self, board: List[List[int]]) -> bool:
        def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def solve() -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        for num in range(1, 10):
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = 0
                        return False
            return True

        return solve()


def get_sudoku() -> Sudoku:
    return Sudoku()
