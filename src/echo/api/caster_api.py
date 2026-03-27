"""强制转换API"""

from fastapi import APIRouter

from echo.research.caster_tool import get_caster_tool


router = APIRouter(prefix="/api/caster", tags=["caster"])


@router.post("/to-int")
async def to_int(value, default: int = 0):
    return {"result": get_caster_tool().to_int(value, default)}


@router.post("/to-float")
async def to_float(value, default: float = 0.0):
    return {"result": get_caster_tool().to_float(value, default)}


@router.post("/to-str")
async def to_str(value):
    return {"result": get_caster_tool().to_str(value)}