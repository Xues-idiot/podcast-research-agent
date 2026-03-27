"""字符串空检查API"""

from fastapi import APIRouter

from echo.research.is_empty_str_tool import get_is_empty_str_tool


router = APIRouter(prefix="/api/is-empty-str", tags=["is-empty-str"])


@router.post("/is-empty")
async def is_empty(text: str):
    return {"result": get_is_empty_str_tool().is_empty(text)}