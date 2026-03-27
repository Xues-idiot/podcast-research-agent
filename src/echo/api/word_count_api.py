"""单词计数API"""

from fastapi import APIRouter

from echo.research.word_count import get_word_count


router = APIRouter(prefix="/api/word-count", tags=["word-count"])


@router.post("/count")
async def count(text: str):
    """计数"""
    tool = get_word_count()
    return {"count": tool.count(text)}
