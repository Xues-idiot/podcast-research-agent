"""图像灰度API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_grayscale import get_image_grayscale_tool


router = APIRouter(prefix="/api/image-grayscale", tags=["image-grayscale"])


class GrayscaleRequest(BaseModel):
    img: list[list[list[float]]]


@router.post("/grayscale")
async def grayscale(request: GrayscaleRequest):
    tool = get_image_grayscale_tool()
    return {"result": tool.grayscale(request.img)}