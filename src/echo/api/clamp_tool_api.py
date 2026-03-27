"""区间限制API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.clamp_tool import get_clamp_tool


router = APIRouter(prefix="/api/clamp-tool", tags=["clamp-tool"])


class ClampRequest(BaseModel):
    value: float
    min_val: float
    max_val: float


@router.post("/clamp")
async def clamp(request: ClampRequest):
    return {"result": get_clamp_tool().clamp(request.value, request.min_val, request.max_val)}
