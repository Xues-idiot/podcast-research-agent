"""替换API"""

from fastapi import APIRouter

from echo.research.replace_tool import get_replace_tool


router = APIRouter(prefix="/api/replace", tags=["replace"])


@router.post("/replace")
async def replace(text: str, old: str, new: str):
    return {"result": get_replace_tool().replace(text, old, new)}