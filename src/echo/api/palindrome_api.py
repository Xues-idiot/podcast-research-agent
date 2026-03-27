"""回文API"""

from fastapi import APIRouter

from echo.research.palindrome import get_palindrome


router = APIRouter(prefix="/api/palindrome", tags=["palindrome"])


@router.post("/check")
async def check(s: str):
    """检查回文"""
    tool = get_palindrome()
    return {"is_palindrome": tool.is_palindrome(s)}


@router.post("/longest")
async def longest(s: str):
    """最长回文子串"""
    tool = get_palindrome()
    return {"longest": tool.longest_palindrome(s)}
