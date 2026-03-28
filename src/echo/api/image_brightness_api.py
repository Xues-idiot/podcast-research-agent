"""图像亮度调整API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_brightness import get_image_brightness_tool


router = APIRouter(prefix="/api/image-brightness", tags=["image-brightness"])


class BrightnessRequest(BaseModel):
    img: list[list[list[float]]]
    factor: float = 1.0


@router.post("/brightness")
async def brightness(request: BrightnessRequest):
    tool = get_image_brightness_tool()
    return {"result": tool.brightness(request.img, request.factor)}