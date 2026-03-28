"""向量叉积API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_cross import get_vector_cross_tool


router = APIRouter(prefix="/api/vector-cross", tags=["vector-cross"])


class CrossRequest(BaseModel):
    a: list[float]
    b: list[float]


@router.post("/cross")
async def cross_product(request: CrossRequest):
    tool = get_vector_cross_tool()
    return {"result": tool.cross(request.a, request.b)}