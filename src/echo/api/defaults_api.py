"""默认值API"""

from fastapi import APIRouter

from echo.research.defaults_tool import get_defaults_tool


router = APIRouter(prefix="/api/defaults", tags=["defaults"])


@router.post("/default")
async def default(value, default_val):
    return {"result": get_defaults_tool().default(value, default_val)}