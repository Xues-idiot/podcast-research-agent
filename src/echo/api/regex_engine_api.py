"""正则表达式引擎API"""

from fastapi import APIRouter

from echo.research.regex_engine import get_regex_engine


router = APIRouter(prefix="/api/regex", tags=["regex"])


@router.post("/match")
async def match(pattern: str, text: str):
    """匹配"""
    tool = get_regex_engine()
    return {"matched": tool.match(pattern, text)}


@router.post("/search")
async def search(pattern: str, text: str):
    """搜索"""
    tool = get_regex_engine()
    return {"found": tool.search(pattern, text)}


@router.post("/replace")
async def replace(pattern: str, text: str, replacement: str):
    """替换"""
    tool = get_regex_engine()
    return {"result": tool.replace(pattern, text, replacement)}
