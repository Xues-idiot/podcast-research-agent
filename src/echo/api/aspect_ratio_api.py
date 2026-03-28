"""宽高比计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.aspect_ratio import get_aspect_ratio_tool


router = APIRouter(prefix="/api/aspect-ratio", tags=["aspect-ratio"])


class RatioRequest(BaseModel):
    width: int
    height: int


@router.post("/calculate")
async def calculate(request: RatioRequest):
    tool = get_aspect_ratio_tool()
    w, h = tool.calculate(request.width, request.height)
    return {"ratio": f"{w}:{h}", "width": w, "height": h}