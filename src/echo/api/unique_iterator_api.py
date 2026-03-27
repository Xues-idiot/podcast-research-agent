"""唯一迭代器API"""

from fastapi import APIRouter

from echo.research.unique_iterator import get_unique_iterator


router = APIRouter(prefix="/api/unique-iter", tags=["unique-iter"])


@router.post("/unique")
async def unique(items: list):
    return {"result": list(get_unique_iterator().unique(iter(items)))}
