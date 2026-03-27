"""信号微分API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.signal_differentiator import get_signal_differentiator


router = APIRouter(prefix="/api/differentiator", tags=["differentiator"])


class DiffRequest(BaseModel):
    signal: list
    dt: float = 1.0


@router.post("/differentiate")
async def differentiate(request: DiffRequest):
    return {"result": get_signal_differentiator().differentiate(request.signal, request.dt)}
