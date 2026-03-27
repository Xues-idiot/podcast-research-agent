"""单词换行API"""

from fastapi import APIRouter

from echo.research.word_wrap import get_word_wrap


router = APIRouter(prefix="/api/word-wrap", tags=["word-wrap"])


@router.post("/wrap")
async def wrap(text: str, width: int = 80):
    """换行"""
    tool = get_word_wrap()
    return {"lines": tool.wrap(text, width)}
