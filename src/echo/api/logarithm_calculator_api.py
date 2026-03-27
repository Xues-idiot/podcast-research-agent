"""对数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.logarithm_calculator import get_logarithm_calculator


router = APIRouter(prefix="/api/log-calc", tags=["log-calc"])


class LogRequest(BaseModel):
    x: float
    base: float = 2.718281828459045


@router.post("/log")
async def log(request: LogRequest):
    return {"result": get_logarithm_calculator().log(request.x, request.base)}
