"""字符统计API"""

from fastapi import APIRouter

from echo.research.character_counter import get_character_counter


router = APIRouter(prefix="/api/chars", tags=["chars"])


@router.post("/count")
async def count_chars(text: str):
    return {"counts": get_character_counter().count_chars(text)}


@router.post("/unique")
async def count_unique(text: str):
    return {"unique_count": get_character_counter().count_unique_chars(text)}


@router.post("/most_common")
async def most_common(text: str, top_n: int = 10):
    return {"most_common": get_character_counter().most_common_chars(text, top_n)}