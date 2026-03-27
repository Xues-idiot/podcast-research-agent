"""开头检查API"""

from fastapi import APIRouter

from echo.research.starts_with_tool import get_starts_with_tool


router = APIRouter(prefix="/api/starts-with", tags=["starts-with"])


@router.post("/starts-with")
async def starts_with(text: str, prefix: str):
    return {"result": get_starts_with_tool().starts_with(text, prefix)}