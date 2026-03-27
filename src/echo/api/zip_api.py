"""Zip API"""

from fastapi import APIRouter

from echo.research.zip_tool import get_zip_tool


router = APIRouter(prefix="/api/zip", tags=["zip"])


@router.post("/zip-lists")
async def zip_lists(*lists: list):
    return {"result": get_zip_tool().zip_lists(*lists)}