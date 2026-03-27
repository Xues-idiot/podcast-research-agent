"""制表符API"""

from fastapi import APIRouter

from echo.research.tabler import get_tabler_tool


router = APIRouter(prefix="/api/tabler", tags=["tabler"])


@router.post("/spaces-to-tabs")
async def spaces_to_tabs(text: str, width: int = 4):
    return {"result": get_tabler_tool().spaces_to_tabs(text, width)}


@router.post("/tabs-to-spaces")
async def tabs_to_spaces(text: str, width: int = 4):
    return {"result": get_tabler_tool().tabs_to_spaces(text, width)}