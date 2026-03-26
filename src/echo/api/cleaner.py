"""文本清理API"""

from fastapi import APIRouter

from echo.research.cleaner import get_text_cleaner


router = APIRouter(prefix="/api/clean", tags=["clean"])


@router.post("/whitespace")
async def remove_whitespace(text: str):
    cleaner = get_text_cleaner()
    return {"result": cleaner.remove_extra_whitespace(text)}


@router.post("/newlines")
async def remove_newlines(text: str):
    cleaner = get_text_cleaner()
    return {"result": cleaner.remove_extra_newlines(text)}


@router.post("/urls")
async def remove_urls(text: str):
    cleaner = get_text_cleaner()
    return {"result": cleaner.remove_urls(text)}


@router.post("/html")
async def remove_html(text: str):
    cleaner = get_text_cleaner()
    return {"result": cleaner.remove_html_tags(text)}


@router.post("/full")
async def full_clean(text: str):
    cleaner = get_text_cleaner()
    return {"result": cleaner.full_clean(text)}