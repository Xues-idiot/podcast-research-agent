"""首字母大写API"""

from fastapi import APIRouter

from echo.research.capitalizer import get_capitalizer


router = APIRouter(prefix="/api/capitalize", tags=["capitalize"])


@router.post("/capitalize")
async def capitalize(text: str):
    """首字母大写"""
    tool = get_capitalizer()
    return {"result": tool.capitalize(text)}


@router.post("/title")
async def title(text: str):
    """标题大写"""
    tool = get_capitalizer()
    return {"result": tool.title_case(text)}
