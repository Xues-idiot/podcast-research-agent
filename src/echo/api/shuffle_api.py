"""打乱API"""

from fastapi import APIRouter

from echo.research.shuffle_tool import get_shuffle_tool


router = APIRouter(prefix="/api/shuffle", tags=["shuffle"])


@router.post("/shuffle")
async def shuffle(items: list):
    return {"result": get_shuffle_tool().shuffle(items)}