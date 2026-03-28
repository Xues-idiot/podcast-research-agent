"""颜色饱和度API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.color_saturation import get_color_saturation_tool


router = APIRouter(prefix="/api/color-saturation", tags=["color-saturation"])


class SaturationRequest(BaseModel):
    hex_color: str
    amount: float = 0.2


@router.post("/saturate")
async def saturate(request: SaturationRequest):
    tool = get_color_saturation_tool()
    return {"result": tool.saturate(request.hex_color, request.amount)}


@router.post("/desaturate")
async def desaturate(request: SaturationRequest):
    tool = get_color_saturation_tool()
    return {"result": tool.desaturate(request.hex_color, request.amount)}