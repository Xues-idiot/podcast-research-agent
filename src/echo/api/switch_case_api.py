"""切换API"""

from fastapi import APIRouter

from echo.research.switch_case import get_switch_case


router = APIRouter(prefix="/api/switch-case", tags=["switch-case"])


@router.post("/switch")
async def switch(value, cases: dict):
    return {"result": get_switch_case().switch(value, cases)}