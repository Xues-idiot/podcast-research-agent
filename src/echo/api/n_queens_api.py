"""N皇后API"""

from fastapi import APIRouter

from echo.research.n_queens import get_n_queens


router = APIRouter(prefix="/api/n-queens", tags=["n-queens"])


@router.post("/solve")
async def solve(n: int):
    """求解N皇后"""
    tool = get_n_queens()
    return {"solutions": tool.solve(n)}
