"""表情符号API"""

from fastapi import APIRouter

from echo.research.emoji_tool import get_emoji_tool


router = APIRouter(prefix="/api/emoji", tags=["emoji"])


@router.post("/random")
async def random_emoji(category: str = "happy"):
    return {"emoji": get_emoji_tool().random_emoji(category)}


@router.post("/add")
async def add_emoji(text: str, category: str = "happy"):
    return {"result": get_emoji_tool().add_emoji(text, category)}