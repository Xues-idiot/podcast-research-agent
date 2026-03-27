"""数独API"""

from fastapi import APIRouter

from echo.research.sudoku import get_sudoku


router = APIRouter(prefix="/api/sudoku", tags=["sudoku"])


@router.post("/solve")
async def solve(board: list):
    """求解数独"""
    tool = get_sudoku()
    return {"solved": tool.solve(board)}
