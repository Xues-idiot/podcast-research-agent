"""文本替换API"""

from fastapi import APIRouter

from echo.research.text_replacer import get_text_replacer


router = APIRouter(prefix="/api/replace", tags=["replace"])


@router.post("/text")
async def replace_text(text: str, old: str, new: str, count: int = -1):
    replacer = get_text_replacer()
    result = replacer.replace(text, old, new, count)
    return {
        "result": result.result_text,
        "replacement_count": result.replacement_count
    }


@router.post("/regex")
async def replace_regex(text: str, pattern: str, replacement: str):
    replacer = get_text_replacer()
    result = replacer.replace_regex(text, pattern, replacement)
    return {
        "result": result.result_text,
        "replacement_count": result.replacement_count
    }


@router.post("/multiple")
async def replace_multiple(text: str, replacements: dict[str, str]):
    replacer = get_text_replacer()
    result = replacer.replace_multiple(text, replacements)
    return {
        "result": result.result_text,
        "replacement_count": result.replacement_count
    }