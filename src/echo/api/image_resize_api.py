"""图像缩放API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_resize import get_image_resize_tool


router = APIRouter(prefix="/api/image-resize", tags=["image-resize"])


class ResizeRequest(BaseModel):
    img: list[list[list[float]]]
    target_h: int
    target_w: int


@router.post("/resize")
async def resize(request: ResizeRequest):
    tool = get_image_resize_tool()
    return {"result": tool.resize(request.img, request.target_h, request.target_w)}