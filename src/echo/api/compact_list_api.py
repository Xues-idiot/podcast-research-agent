"""压缩列表API"""

from fastapi import APIRouter

from echo.research.compact_list import get_compact_list


router = APIRouter(prefix="/api/compact-list", tags=["compact-list"])


@router.post("/compact")
async def compact(items: list):
    return {"result": get_compact_list().compact(items)}
