"""正则表达式API"""

from fastapi import APIRouter

from echo.research.regex_helper import get_regex_helper


router = APIRouter(prefix="/api/regex", tags=["regex"])


@router.post("/find")
async def find_matches(text: str, pattern: str):
    return {"matches": get_regex_helper().find_all_matches(text, pattern)}


@router.post("/find_with_context")
async def find_with_context(text: str, pattern: str, context_chars: int = 50):
    return {"matches": get_regex_helper().find_with_context(text, pattern, context_chars)}


@router.post("/split")
async def split_by_pattern(text: str, pattern: str):
    return {"parts": get_regex_helper().split_by_pattern(text, pattern)}