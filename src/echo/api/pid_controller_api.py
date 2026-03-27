"""PID控制API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pid_controller import get_pid_controller


router = APIRouter(prefix="/api/pid", tags=["pid"])


class PidRequest(BaseModel):
    setpoint: float
    current: float
    kp: float = 1.0
    ki: float = 0.0
    kd: float = 0.0


@router.post("/compute")
async def compute(request: PidRequest):
    result, integral, error = get_pid_controller().compute(
        request.setpoint, request.current, request.kp, request.ki, request.kd
    )
    return {"output": result, "integral": integral, "error": error}
