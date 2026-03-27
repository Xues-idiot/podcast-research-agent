"""扁平化API"""

from fastapi import APIRouter

from echo.research.flatten_tool import get_flatten_tool


router = APIRouter(prefix="/api/flatten", tags=["flatten"])


@router.post("/flatten")
async def flatten(items: list):
    return {"result": get_flatten_tool().flatten(items)}