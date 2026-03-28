"""矩阵迹API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_trace import get_matrix_trace_tool


router = APIRouter(prefix="/api/matrix-trace", tags=["matrix-trace"])


class TraceRequest(BaseModel):
    matrix: list[list[float]]


@router.post("/trace")
async def trace(request: TraceRequest):
    tool = get_matrix_trace_tool()
    return {"result": tool.trace(request.matrix)}