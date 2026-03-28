"""图像旋转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_rotate import get_image_rotate_tool


router = APIRouter(prefix="/api/image-rotate", tags=["image-rotate"])


class Rotate90Request(BaseModel):
    img: list[list[list[float]]]
    clockwise: bool = True


class Rotate180Request(BaseModel):
    img: list[list[list[float]]]


@router.post("/rotate-90")
async def rotate_90(request: Rotate90Request):
    tool = get_image_rotate_tool()
    return {"result": tool.rotate_90(request.img, request.clockwise)}


@router.post("/rotate-180")
async def rotate_180(request: Rotate180Request):
    tool = get_image_rotate_tool()
    return {"result": tool.rotate_180(request.img)}