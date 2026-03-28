"""向量钳制API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_clamp import get_vector_clamp_tool


router = APIRouter(prefix="/api/vector-clamp", tags=["vector-clamp"])


class ClampRequest(BaseModel):
    v: list[float]
    min_val: float
    max_val: float


@router.post("/clamp")
async def clamp(request: ClampRequest):
    tool = get_vector_clamp_tool()
    return {"result": tool.clamp(request.v, request.min_val, request.max_val)}