"""向量模长API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_magnitude import get_vector_magnitude_tool


router = APIRouter(prefix="/api/vector-magnitude", tags=["vector-magnitude"])


class MagnitudeRequest(BaseModel):
    v: list[float]


@router.post("/magnitude")
async def magnitude(request: MagnitudeRequest):
    tool = get_vector_magnitude_tool()
    return {"result": tool.magnitude(request.v)}