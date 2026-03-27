"""绝对值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.absolute_value import get_absolute_value


router = APIRouter(prefix="/api/absolute-value", tags=["absolute-value"])


class AbsRequest(BaseModel):
    n: float


@router.post("/abs")
async def abs(request: AbsRequest):
    return {"result": get_absolute_value().abs(request.n)}
