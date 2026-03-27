"""两数之和API"""

from fastapi import APIRouter

from echo.research.two_sum import get_two_sum


router = APIRouter(prefix="/api/two-sum", tags=["two-sum"])


@router.post("/solve")
async def solve(nums: list, target: int):
    """求解两数之和"""
    tool = get_two_sum()
    return {"indices": tool.solve(nums, target)}
