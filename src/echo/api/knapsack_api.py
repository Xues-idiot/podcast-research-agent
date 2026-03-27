"""背包问题API"""

from fastapi import APIRouter

from echo.research.knapsack import get_knapsack


router = APIRouter(prefix="/api/knapsack", tags=["knapsack"])


@router.post("/0-1")
async def solve_0_1(weights: list, values: list, capacity: int):
    """0-1背包"""
    tool = get_knapsack()
    return {"result": tool.solve_0_1(weights, values, capacity)}


@router.post("/unbounded")
async def solve_unbounded(weights: list, values: list, capacity: int):
    """无限背包"""
    tool = get_knapsack()
    return {"result": tool.solve_unbounded(weights, values, capacity)}
