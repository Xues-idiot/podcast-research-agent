"""N皇后工具"""

from typing import List, Optional


class NQueens:
    _instance: Optional["NQueens"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def solve(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def is_safe(board: List[List[str]], row: int, col: int) -> bool:
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            return True

        def solve_col(col: int):
            if col == n:
                result.append(["".join(row) for row in board])
                return
            for row in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    solve_col(col + 1)
                    board[row][col] = "."

        solve_col(0)
        return result


def get_n_queens() -> NQueens:
    return NQueens()
