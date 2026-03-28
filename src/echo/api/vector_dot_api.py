"""向量点积API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_dot import get_vector_dot_tool


router = APIRouter(prefix="/api/vector-dot", tags=["vector-dot"])


class DotRequest(BaseModel):
    a: list[float]
    b: list[float]


@router.post("/dot")
async def dot_product(request: DotRequest):
    tool = get_vector_dot_tool()
    return {"result": tool.dot(request.a, request.b)}