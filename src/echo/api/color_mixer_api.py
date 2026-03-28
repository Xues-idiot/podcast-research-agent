"""颜色混合API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.color_mixer import get_color_mixer_tool


router = APIRouter(prefix="/api/color-mixer", tags=["color-mixer"])


class MixRequest(BaseModel):
    color1: str
    color2: str
    ratio: float = 0.5


@router.post("/mix")
async def mix(request: MixRequest):
    tool = get_color_mixer_tool()
    return {"result": tool.mix(request.color1, request.color2, request.ratio)}