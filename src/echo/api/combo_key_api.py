"""组合键API"""

from fastapi import APIRouter

from echo.research.combo_key import get_combo_key_tool


router = APIRouter(prefix="/api/combo-key", tags=["combo-key"])


@router.post("/make")
async def make_combo(*keys):
    return {"result": get_combo_key_tool().make_combo(*keys)}


@router.post("/to-str")
async def combo_to_str(combo: tuple):
    return {"result": get_combo_key_tool().combo_to_str(combo)}