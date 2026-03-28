"""图像边缘检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_edge import get_image_edge_tool


router = APIRouter(prefix="/api/image-edge", tags=["image-edge"])


class EdgeRequest(BaseModel):
    img: list[list[list[float]]]


@router.post("/sobel")
async def sobel(request: EdgeRequest):
    tool = get_image_edge_tool()
    return {"result": tool.sobel(request.img)}