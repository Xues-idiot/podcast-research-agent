"""采样生成API"""

from fastapi import APIRouter

from echo.research.sample_gen import get_sample_gen


router = APIRouter(prefix="/api/sample-gen", tags=["sample-gen"])


@router.post("/sample")
async def sample(items: list, count: int, replace: bool = False):
    """采样"""
    tool = get_sample_gen()
    return {"result": tool.sample(items, count, replace)}
