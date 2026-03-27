"""开关工具API"""

from fastapi import APIRouter

from echo.research.switch_tool import get_switch_tool


router = APIRouter(prefix="/api/switch", tags=["switch"])


@router.post("/add-case")
async def add_case(key, value):
    get_switch_tool().add_case(key, value)
    return {"success": True}


@router.get("/get")
async def get_value(key, default=None):
    return {"result": get_switch_tool().get(key, default)}