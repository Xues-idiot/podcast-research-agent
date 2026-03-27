"""标志工具API"""

from fastapi import APIRouter

from echo.research.flag_tool import get_flag_tool


router = APIRouter(prefix="/api/flag", tags=["flag"])


@router.post("/set")
async def set_flag(name: str, value: bool = True):
    get_flag_tool().set_flag(name, value)
    return {"success": True}


@router.get("/get")
async def get_flag(name: str):
    return {"value": get_flag_tool().get_flag(name)}


@router.post("/toggle")
async def toggle_flag(name: str):
    return {"value": get_flag_tool().toggle_flag(name)}