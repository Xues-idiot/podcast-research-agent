"""最长递增子序列API"""

from fastapi import APIRouter

from echo.research.LIS import get_lis


router = APIRouter(prefix="/api/lis", tags=["lis"])


@router.post("/length")
async def length(nums: list):
    """LIS长度"""
    tool = get_lis()
    return {"length": tool.length(nums)}
