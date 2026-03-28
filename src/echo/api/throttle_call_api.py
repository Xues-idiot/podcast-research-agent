"""节流调用API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.throttle_call import get_throttle_call_tool


router = APIRouter(prefix="/api/throttle-call", tags=["throttle-call"])


class ThrottleRequest(BaseModel):
    interval: float


@router.post("/throttle")
async def throttle(request: ThrottleRequest):
    tool = get_throttle_call_tool()
    return {"message": "Throttle configured", "interval": request.interval}