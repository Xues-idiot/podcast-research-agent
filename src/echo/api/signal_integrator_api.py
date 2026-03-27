"""信号积分API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.signal_integrator import get_signal_integrator


router = APIRouter(prefix="/api/integrator", tags=["integrator"])


class IntegratorRequest(BaseModel):
    signal: list
    dt: float = 1.0


@router.post("/integrate")
async def integrate(request: IntegratorRequest):
    return {"result": get_signal_integrator().integrate(request.signal, request.dt)}
