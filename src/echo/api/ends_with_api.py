"""结尾检查API"""

from fastapi import APIRouter

from echo.research.ends_with_tool import get_ends_with_tool


router = APIRouter(prefix="/api/ends-with", tags=["ends-with"])


@router.post("/ends-with")
async def ends_with(text: str, suffix: str):
    return {"result": get_ends_with_tool().ends_with(text, suffix)}