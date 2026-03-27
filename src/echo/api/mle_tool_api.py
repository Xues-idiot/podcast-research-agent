"""最大似然估计API"""

from fastapi import APIRouter

from echo.research.mle_tool import get_mle_tool


router = APIRouter(prefix="/api/mle", tags=["mle"])


@router.post("/normal")
async def normal(data: list):
    return {"result": get_mle_tool().normal_mle(data)}
