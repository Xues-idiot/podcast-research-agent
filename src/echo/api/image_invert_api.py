"""图像反色API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_invert import get_image_invert_tool


router = APIRouter(prefix="/api/image-invert", tags=["image-invert"])


class InvertRequest(BaseModel):
    img: list[list[list[float]]]


@router.post("/invert")
async def invert(request: InvertRequest):
    tool = get_image_invert_tool()
    return {"result": tool.invert(request.img)}