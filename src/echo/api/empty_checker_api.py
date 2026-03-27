"""空检查API"""

from fastapi import APIRouter

from echo.research.empty_checker import get_empty_checker


router = APIRouter(prefix="/api/empty-checker", tags=["empty-checker"])


@router.post("/is-empty")
async def is_empty(value):
    return {"result": get_empty_checker().is_empty(value)}