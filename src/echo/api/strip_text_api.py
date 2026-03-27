"""去除空白API"""

from fastapi import APIRouter

from echo.research.strip_text import get_strip_text


router = APIRouter(prefix="/api/strip", tags=["strip"])


@router.post("/strip")
async def strip(text: str):
    """去除空白"""
    tool = get_strip_text()
    return {"result": tool.strip(text)}


@router.post("/normalize")
async def normalize(text: str):
    """规范化空白"""
    tool = get_strip_text()
    return {"result": tool.normalize(text)}
