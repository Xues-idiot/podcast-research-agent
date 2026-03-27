"""采样API"""

from fastapi import APIRouter

from echo.research.sample_list import get_sample_list


router = APIRouter(prefix="/api/sample", tags=["sample"])


@router.post("/items")
async def sample_items(items: list, n: int, replace: bool = False):
    """采样元素"""
    tool = get_sample_list()
    return {"items": tool.sample(items, n, replace)}


@router.post("/one")
async def sample_one(items: list):
    """随机选一个"""
    tool = get_sample_list()
    return {"item": tool.sample_one(items)}
