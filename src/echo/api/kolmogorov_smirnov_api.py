"""KS检验API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.kolmogorov_smirnov import get_kolmogorov_smirnov


router = APIRouter(prefix="/api/ks-test", tags=["ks-test"])


class KSRequest(BaseModel):
    data: list


@router.post("/statistic")
async def statistic(request: KSRequest):
    return {"result": get_kolmogorov_smirnov().ks_statistic(request.data, lambda x: 0.5)}
