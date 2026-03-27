"""布隆过滤器API"""

from fastapi import APIRouter

from echo.research.bloom_filter import get_bloom_filter


router = APIRouter(prefix="/api/bloom", tags=["bloom"])


@router.post("/add")
async def add(item: str):
    """添加元素"""
    tool = get_bloom_filter()
    tool.add(item)
    return {"success": True}


@router.post("/contains")
async def contains(item: str):
    """检查包含"""
    tool = get_bloom_filter()
    return {"contains": tool.contains(item)}
