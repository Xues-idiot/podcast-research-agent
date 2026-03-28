"""向量旋转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_rotate import get_vector_rotate_tool


router = APIRouter(prefix="/api/vector-rotate", tags=["vector-rotate"])


class Rotate2DRequest(BaseModel):
    v: list[float]
    angle: float


class Rotate3DRequest(BaseModel):
    v: list[float]
    axis: list[float]
    angle: float


@router.post("/rotate-2d")
async def rotate_2d(request: Rotate2DRequest):
    tool = get_vector_rotate_tool()
    return {"result": tool.rotate_2d(request.v, request.angle)}


@router.post("/rotate-3d")
async def rotate_3d(request: Rotate3DRequest):
    tool = get_vector_rotate_tool()
    return {"result": tool.rotate_3d(request.v, request.axis, request.angle)}