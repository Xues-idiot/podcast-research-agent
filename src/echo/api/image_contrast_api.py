"""图像对比度调整API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_contrast import get_image_contrast_tool


router = APIRouter(prefix="/api/image-contrast", tags=["image-contrast"])


class ContrastRequest(BaseModel):
    img: list[list[list[float]]]
    factor: float = 1.0


@router.post("/contrast")
async def contrast(request: ContrastRequest):
    tool = get_image_contrast_tool()
    return {"result": tool.contrast(request.img, request.factor)}