"""唯一生成API"""

from fastapi import APIRouter

from echo.research.unique_gen import get_unique_gen


router = APIRouter(prefix="/api/unique-gen", tags=["unique-gen"])


@router.post("/unique")
async def unique(items: list):
    """去重"""
    tool = get_unique_gen()
    return {"result": tool.unique(items)}
