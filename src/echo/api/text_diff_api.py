"""文本差异API"""

from fastapi import APIRouter

from echo.research.text_diff import get_text_diff


router = APIRouter(prefix="/api/text-diff", tags=["text-diff"])


@router.post("/diff")
async def diff(text1: str, text2: str):
    """差异比较"""
    tool = get_text_diff()
    return {"diff": tool.diff_lines(text1, text2)}
