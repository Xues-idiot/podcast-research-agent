"""Zip API"""

from fastapi import APIRouter

from echo.research.zippable_tool import get_zippable_tool


router = APIRouter(prefix="/api/zippable", tags=["zippable"])


@router.post("/zip")
async def zip_lists(*lists: list):
    return {"result": get_zippable_tool().zip_lists(*lists)}