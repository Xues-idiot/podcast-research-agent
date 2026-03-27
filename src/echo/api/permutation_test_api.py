"""排列检验API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.permutation_test import get_permutation_test


router = APIRouter(prefix="/api/permutation", tags=["permutation"])


class PermuteRequest(BaseModel):
    data: list
    n: int


@router.post("/permute")
async def permute(request: PermuteRequest):
    return {"result": get_permutation_test().permute(request.data, request.n)}
