"""打乱生成API"""

from fastapi import APIRouter

from echo.research.shuffle_gen import get_shuffle_gen


router = APIRouter(prefix="/api/shuffle-gen", tags=["shuffle-gen"])


@router.post("/shuffle")
async def shuffle(items: list):
    """打乱"""
    tool = get_shuffle_gen()
    return {"result": tool.shuffle(items)}
