"""图像阈值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_threshold import get_image_threshold_tool


router = APIRouter(prefix="/api/image-threshold", tags=["image-threshold"])


class ThresholdRequest(BaseModel):
    img: list[list[list[float]]]
    value: float = 0.5


@router.post("/threshold")
async def threshold(request: ThresholdRequest):
    tool = get_image_threshold_tool()
    return {"result": tool.threshold(request.img, request.value)}