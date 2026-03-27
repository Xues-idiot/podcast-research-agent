"""空值API"""

from fastapi import APIRouter

from echo.research.empty_tool import get_empty_tool


router = APIRouter(prefix="/api/empty", tags=["empty"])


@router.post("/is-empty")
async def is_empty(value):
    return {"result": get_empty_tool().is_empty(value)}