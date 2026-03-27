"""百分位数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.percentile_calculator import get_percentile_calculator


router = APIRouter(prefix="/api/percentile-calc", tags=["percentile-calc"])


class PercentileRequest(BaseModel):
    items: list
    p: float


@router.post("/percentile")
async def percentile(request: PercentileRequest):
    return {"result": get_percentile_calculator().percentile(request.items, request.p)}
