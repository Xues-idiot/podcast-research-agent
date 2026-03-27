"""文本标准化API"""

from fastapi import APIRouter

from echo.research.text_normalizer import get_text_normalizer


router = APIRouter(prefix="/api/normalize", tags=["normalize"])


@router.post("/whitespace")
async def normalize_whitespace(text: str):
    normalizer = get_text_normalizer()
    return {"result": normalizer.normalize_whitespace(text)}


@router.post("/newlines")
async def normalize_newlines(text: str, max_consecutive: int = 2):
    normalizer = get_text_normalizer()
    return {"result": normalizer.normalize_newlines(text, max_consecutive)}


@router.post("/full")
async def full_normalize(text: str):
    normalizer = get_text_normalizer()
    return {"result": normalizer.full_normalize(text)}