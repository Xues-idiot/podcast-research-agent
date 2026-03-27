"""四舍五入API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.round_calculator import get_round_calculator


router = APIRouter(prefix="/api/round-calc", tags=["round-calc"])


class RoundRequest(BaseModel):
    n: float
    decimals: int = 0


@router.post("/round")
async def round_val(request: RoundRequest):
    return {"result": get_round_calculator().round_val(request.n, request.decimals)}
