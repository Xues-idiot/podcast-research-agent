"""交错API"""

from fastapi import APIRouter

from echo.research.interleave import get_interleave


router = APIRouter(prefix="/api/interleave", tags=["interleave"])


@router.post("/lists")
async def interleave_lists(lists: list):
    """交错多个列表"""
    tool = get_interleave()
    return {"result": tool.interleave(*lists)}


@router.post("/interpose")
async def interpose_list(items: list, sep: str):
    """在元素间插入分隔符"""
    tool = get_interleave()
    return {"result": tool.interpose(items, sep)}
