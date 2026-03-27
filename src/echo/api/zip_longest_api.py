"""Zip最长API"""

from fastapi import APIRouter

from echo.research.zip_longest_tool import get_zip_longest_tool


router = APIRouter(prefix="/api/zip-longest", tags=["zip-longest"])


@router.post("/zip-longest")
async def zip_longest(*lists: list, fillvalue=None):
    return {"result": get_zip_longest_tool().zip_longest(*lists, fillvalue=fillvalue)}