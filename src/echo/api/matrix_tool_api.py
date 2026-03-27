"""矩阵API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_tool import get_matrix_tool


router = APIRouter(prefix="/api/matrix-tool", tags=["matrix-tool"])


class TransposeRequest(BaseModel):
    matrix: list


@router.post("/transpose")
async def transpose(request: TransposeRequest):
    return {"result": get_matrix_tool().transpose(request.matrix)}
