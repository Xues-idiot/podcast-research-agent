"""颜色变亮API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.color_lighten import get_color_lighten_tool


router = APIRouter(prefix="/api/color-lighten", tags=["color-lighten"])


class LightenRequest(BaseModel):
    hex_color: str
    amount: float = 0.2


@router.post("/lighten")
async def lighten(request: LightenRequest):
    tool = get_color_lighten_tool()
    return {"result": tool.lighten(request.hex_color, request.amount)}


@router.post("/darken")
async def darken(request: LightenRequest):
    tool = get_color_lighten_tool()
    return {"result": tool.darken(request.hex_color, request.amount)}