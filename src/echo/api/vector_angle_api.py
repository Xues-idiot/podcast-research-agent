"""向量角度API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_angle import get_vector_angle_tool


router = APIRouter(prefix="/api/vector-angle", tags=["vector-angle"])


class AngleRequest(BaseModel):
    a: list[float]
    b: list[float]


@router.post("/angle")
async def angle(request: AngleRequest):
    tool = get_vector_angle_tool()
    return {"result": tool.angle(request.a, request.b)}