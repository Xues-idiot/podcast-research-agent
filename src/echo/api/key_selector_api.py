"""键选择器API"""

from fastapi import APIRouter

from echo.research.key_selector import get_key_selector


router = APIRouter(prefix="/api/key-selector", tags=["key-selector"])


@router.post("/select-keys")
async def select_keys(item: dict, keys: list):
    return {"result": get_key_selector().select_keys(item, keys)}