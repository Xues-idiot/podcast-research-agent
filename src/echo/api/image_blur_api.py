"""图像模糊API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_blur import get_image_blur_tool


router = APIRouter(prefix="/api/image-blur", tags=["image-blur"])


class BlurRequest(BaseModel):
    img: list[list[list[float]]]
    radius: int = 3


@router.post("/blur")
async def blur(request: BlurRequest):
    tool = get_image_blur_tool()
    return {"result": tool.blur(request.img, request.radius)}