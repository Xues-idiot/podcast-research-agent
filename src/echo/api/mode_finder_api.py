"""众数API"""

from fastapi import APIRouter

from echo.research.mode_finder import get_mode_finder


router = APIRouter(prefix="/api/mode-finder", tags=["mode-finder"])


@router.post("/mode")
async def mode(items: list):
    return {"result": get_mode_finder().mode(items)}
