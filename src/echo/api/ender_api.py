"""结束符API"""

from fastapi import APIRouter

from echo.research.ender import get_ender_tool


router = APIRouter(prefix="/api/ender", tags=["ender"])


@router.post("/add-period")
async def add_period(text: str):
    return {"result": get_ender_tool().add_period(text)}


@router.post("/add-question")
async def add_question(text: str):
    return {"result": get_ender_tool().add_question(text)}


@router.post("/add-exclamation")
async def add_exclamation(text: str):
    return {"result": get_ender_tool().add_exclamation(text)}