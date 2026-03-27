"""环状缓冲API"""

from fastapi import APIRouter

from echo.research.ring_buf import get_ring_buf


router = APIRouter(prefix="/api/ring-buf", tags=["ring-buf"])


@router.post("/create")
async def create(capacity: int):
    """创建环状缓冲"""
    tool = get_ring_buf()
    return {"buffer": tool.create(capacity)}
