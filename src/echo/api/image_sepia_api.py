"""图像复古色调API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_sepia import get_image_sepia_tool


router = APIRouter(prefix="/api/image-sepia", tags=["image-sepia"])


class SepiaRequest(BaseModel):
    img: list[list[list[float]]]


@router.post("/sepia")
async def sepia(request: SepiaRequest):
    tool = get_image_sepia_tool()
    return {"result": tool.sepia(request.img)}