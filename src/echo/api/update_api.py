"""更新API"""

from fastapi import APIRouter

from echo.research.update_tool import get_update_tool


router = APIRouter(prefix="/api/update", tags=["update"])


@router.post("/update")
async def update(data: dict, updates: dict):
    return {"result": get_update_tool().update(data, updates)}