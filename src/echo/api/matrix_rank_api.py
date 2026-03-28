"""矩阵秩API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_rank import get_matrix_rank_tool


router = APIRouter(prefix="/api/matrix-rank", tags=["matrix-rank"])


class RankRequest(BaseModel):
    matrix: list[list[float]]


@router.post("/rank")
async def rank(request: RankRequest):
    tool = get_matrix_rank_tool()
    return {"result": tool.rank(request.matrix)}