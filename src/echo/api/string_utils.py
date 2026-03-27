"""字符串工具API"""

from fastapi import APIRouter

from echo.research.string_utils import get_string_utils


router = APIRouter(prefix="/api/string", tags=["string"])


@router.post("/reverse")
async def reverse(text: str):
    return {"result": get_string_utils().reverse(text)}


@router.post("/is_palindrome")
async def is_palindrome(text: str):
    return {"result": get_string_utils().is_palindrome(text)}


@router.post("/count_vowels")
async def count_vowels(text: str):
    return {"count": get_string_utils().count_vowels(text)}


@router.post("/capitalize_words")
async def capitalize_words(text: str):
    return {"result": get_string_utils().capitalize_words(text)}