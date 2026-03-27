"""反转文本API"""

from fastapi import APIRouter

from echo.research.reverse_text import get_reverse_text


router = APIRouter(prefix="/api/reverse-text", tags=["reverse-text"])


@router.post("/reverse")
async def reverse(text: str):
    """反转"""
    tool = get_reverse_text()
    return {"result": tool.reverse(text)}


@router.post("/words")
async def reverse_words(text: str):
    """反转单词"""
    tool = get_reverse_text()
    return {"result": tool.reverse_words(text)}
