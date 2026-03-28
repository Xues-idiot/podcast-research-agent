"""图像直方图API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_histogram import get_image_histogram_tool


router = APIRouter(prefix="/api/image-histogram", tags=["image-histogram"])


class HistogramRequest(BaseModel):
    img: list[list[list[float]]]
    bins: int = 256


@router.post("/histogram")
async def histogram(request: HistogramRequest):
    tool = get_image_histogram_tool()
    return {"result": tool.histogram(request.img, request.bins)}