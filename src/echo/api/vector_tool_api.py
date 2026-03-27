"""向量API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_tool import get_vector_tool


router = APIRouter(prefix="/api/vector-tool", tags=["vector-tool"])


class MagnitudeRequest(BaseModel):
    v: list


@router.post("/magnitude")
async def magnitude(request: MagnitudeRequest):
    return {"result": get_vector_tool().magnitude(request.v)}
