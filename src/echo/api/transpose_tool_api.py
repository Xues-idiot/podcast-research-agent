"""转置API"""

from fastapi import APIRouter

from echo.research.transpose_tool import get_transpose_tool


router = APIRouter(prefix="/api/transpose", tags=["transpose"])


@router.post("/transpose")
async def transpose(matrix: list):
    return {"result": get_transpose_tool().transpose(matrix)}
