"""正则表达式模式API"""

from fastapi import APIRouter

from echo.research.regex_patterns import get_regex_patterns


router = APIRouter(prefix="/api/regex_patterns", tags=["regex_patterns"])


@router.get("/find")
async def find(pattern: str, text: str):
    return {"matches": get_regex_patterns().find_all(pattern, text)}


@router.get("/match")
async def match(pattern: str, text: str):
    return {"is_match": get_regex_patterns().is_match(pattern, text)}