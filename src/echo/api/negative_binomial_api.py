"""负二项分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.negative_binomial import get_negative_binomial


router = APIRouter(prefix="/api/negative-binomial", tags=["negative-binomial"])


class NBRequest(BaseModel):
    k: int
    r: int
    p: float


@router.post("/pmf")
async def pmf(request: NBRequest):
    return {"result": get_negative_binomial().pmf(request.k, request.r, request.p)}
