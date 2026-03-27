"""线性插值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.lerp_tool import get_lerp_tool


router = APIRouter(prefix="/api/lerp-tool", tags=["lerp-tool"])


class LerpRequest(BaseModel):
    a: float
    b: float
    t: float


@router.post("/lerp")
async def lerp(request: LerpRequest):
    return {"result": get_lerp_tool().lerp(request.a, request.b, request.t)}
