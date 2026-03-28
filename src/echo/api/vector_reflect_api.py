"""向量反射API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_reflect import get_vector_reflect_tool


router = APIRouter(prefix="/api/vector-reflect", tags=["vector-reflect"])


class ReflectRequest(BaseModel):
    v: list[float]
    normal: list[float]


@router.post("/reflect")
async def reflect(request: ReflectRequest):
    tool = get_vector_reflect_tool()
    return {"result": tool.reflect(request.v, request.normal)}