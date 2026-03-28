"""延迟工具API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.delay_timer import get_delay_timer_tool


router = APIRouter(prefix="/api/delay-timer", tags=["delay-timer"])


class DelayRequest(BaseModel):
    seconds: float


class CalculateRequest(BaseModel):
    from_rate: float
    to_rate: float
    samples: int


@router.post("/delay")
async def delay(request: DelayRequest):
    tool = get_delay_timer_tool()
    await tool.delay(request.seconds)
    return {"message": "Delay completed"}


@router.post("/calculate")
async def calculate(request: CalculateRequest):
    tool = get_delay_timer_tool()
    result = tool.calculate_delay(request.from_rate, request.to_rate, request.samples)
    return {"delay_seconds": result}