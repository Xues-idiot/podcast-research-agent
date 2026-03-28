"""图像裁剪API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_crop import get_image_crop_tool


router = APIRouter(prefix="/api/image-crop", tags=["image-crop"])


class CropRequest(BaseModel):
    img: list[list[list[float]]]
    x: int
    y: int
    w: int
    h: int


@router.post("/crop")
async def crop(request: CropRequest):
    tool = get_image_crop_tool()
    return {"result": tool.crop(request.img, request.x, request.y, request.w, request.h)}