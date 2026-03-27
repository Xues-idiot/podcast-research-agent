"""深度扁平化API"""

from fastapi import APIRouter

from echo.research.flatten_deep_tool import get_flatten_deep_tool


router = APIRouter(prefix="/api/flatten-deep", tags=["flatten-deep"])


@router.post("/flatten")
async def flatten_deep(items: list):
    return {"result": get_flatten_deep_tool().flatten_deep(items)}