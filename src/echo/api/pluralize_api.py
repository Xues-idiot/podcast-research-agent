"""复数化API"""

from fastapi import APIRouter

from echo.research.pluralize import get_pluralize


router = APIRouter(prefix="/api/pluralize", tags=["pluralize"])


@router.post("/pluralize")
async def pluralize(word: str, count: int):
    """复数化"""
    tool = get_pluralize()
    return {"result": tool.pluralize(word, count)}
