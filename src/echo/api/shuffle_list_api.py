"""打乱API"""

from fastapi import APIRouter

from echo.research.shuffle_list import get_shuffle_list


router = APIRouter(prefix="/api/shuffle", tags=["shuffle"])


@router.post("/list")
async def shuffle_list(items: list):
    """打乱列表"""
    tool = get_shuffle_list()
    return {"items": tool.shuffle(items)}
