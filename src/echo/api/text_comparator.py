"""文本比较API"""

from fastapi import APIRouter

from echo.research.text_comparator import get_text_comparator


router = APIRouter(prefix="/api/compare", tags=["compare"])


@router.post("/similarity")
async def similarity(text1: str, text2: str):
    comp = get_text_comparator()
    return {"ratio": round(comp.similarity_ratio(text1, text2), 4)}


@router.post("/levenshtein")
async def levenshtein(text1: str, text2: str):
    comp = get_text_comparator()
    return {"distance": comp.levenshtein_distance(text1, text2)}


@router.post("/lcs")
async def longest_common_substring(text1: str, text2: str):
    comp = get_text_comparator()
    return {"substring": comp.longest_common_substring(text1, text2)}