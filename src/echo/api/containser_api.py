"""包含检查API"""

from fastapi import APIRouter

from echo.research.containser import get_containser_tool


router = APIRouter(prefix="/api/containser", tags=["containser"])


@router.post("/contains")
async def contains(text: str, substring: str):
    return {"result": get_containser_tool().contains(text, substring)}


@router.post("/contains-any")
async def contains_any(text: str, substrings: list):
    return {"result": get_containser_tool().contains_any(text, substrings)}


@router.post("/contains-all")
async def contains_all(text: str, substrings: list):
    return {"result": get_containser_tool().contains_all(text, substrings)}