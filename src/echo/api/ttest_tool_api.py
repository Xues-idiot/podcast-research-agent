"""t检验API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.ttest_tool import get_ttest_tool


router = APIRouter(prefix="/api/ttest", tags=["ttest"])


class TTestRequest(BaseModel):
    sample: list
    pop_mean: float = 0


@router.post("/one-sample")
async def one_sample(request: TTestRequest):
    return {"result": get_ttest_tool().one_sample_t(request.sample, request.pop_mean)}
