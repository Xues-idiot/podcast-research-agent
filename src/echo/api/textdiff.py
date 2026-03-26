"""文本差异API"""

from fastapi import APIRouter

from echo.research.textdiff import get_text_diff


router = APIRouter(prefix="/api/diff", tags=["diff"])


@router.post("/compare")
async def compare_texts(text1: str, text2: str):
    differ = get_text_diff()
    diffs = differ.diff(text1, text2)
    return {
        "diffs": [
            {"operation": d.operation, "text": d.text}
            for d in diffs
        ]
    }


@router.post("/summary")
async def diff_summary(text1: str, text2: str):
    differ = get_text_diff()
    return differ.diff_summary(text1, text2)