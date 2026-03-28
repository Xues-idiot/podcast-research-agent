"""图像翻转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_flip import get_image_flip_tool


router = APIRouter(prefix="/api/image-flip", tags=["image-flip"])


class FlipRequest(BaseModel):
    img: list[list[list[float]]]


@router.post("/flip-horizontal")
async def flip_horizontal(request: FlipRequest):
    tool = get_image_flip_tool()
    return {"result": tool.flip_horizontal(request.img)}


@router.post("/flip-vertical")
async def flip_vertical(request: FlipRequest):
    tool = get_image_flip_tool()
    return {"result": tool.flip_vertical(request.img)}