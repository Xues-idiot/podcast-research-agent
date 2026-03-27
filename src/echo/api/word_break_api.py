"""单词拆分API"""

from fastapi import APIRouter

from echo.research.word_break import get_word_break


router = APIRouter(prefix="/api/word-break", tags=["word-break"])


@router.post("/can-break")
async def can_break(s: str, words: list):
    """能否拆分"""
    tool = get_word_break()
    return {"can_break": tool.can_break(s, words)}
