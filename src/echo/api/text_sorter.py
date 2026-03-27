"""文本排序API"""

from fastapi import APIRouter

from echo.research.text_sorter import get_text_sorter


router = APIRouter(prefix="/api/sort", tags=["sort"])


@router.post("/lines")
async def sort_lines(lines: list[str], reverse: bool = False):
    sorter = get_text_sorter()
    return {"lines": sorter.sort_lines(lines, reverse)}


@router.post("/by_length")
async def sort_by_length(lines: list[str], reverse: bool = False):
    sorter = get_text_sorter()
    return {"lines": sorter.sort_by_length(lines, reverse)}


@router.post("/alphanumeric")
async def sort_alphanumeric(lines: list[str], reverse: bool = False):
    sorter = get_text_sorter()
    return {"lines": sorter.sort_alphanumeric(lines, reverse)}