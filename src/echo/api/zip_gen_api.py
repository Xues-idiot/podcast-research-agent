"""Zip生成API"""

from fastapi import APIRouter

from echo.research.zip_gen import get_zip_gen


router = APIRouter(prefix="/api/zip-gen", tags=["zip-gen"])


@router.post("/zip")
async def zip_lists(lists: list):
    """Zip"""
    tool = get_zip_gen()
    return {"result": tool.zip(*lists)}
