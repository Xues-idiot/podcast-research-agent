"""图像任意角度旋转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_rotate_any import get_image_rotate_any_tool


router = APIRouter(prefix="/api/image-rotate-any", tags=["image-rotate-any"])


class RotateRequest(BaseModel):
    img: list[list[list[float]]]
    angle: float


@router.post("/rotate")
async def rotate(request: RotateRequest):
    tool = get_image_rotate_any_tool()
    return {"result": tool.rotate(request.img, request.angle)}