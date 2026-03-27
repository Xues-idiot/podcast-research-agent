"""Welch方法API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.welch_method import get_welch_method


router = APIRouter(prefix="/api/welch", tags=["welch"])


class WelchRequest(BaseModel):
    signal: list
    nperseg: int = 256


@router.post("/psd")
async def psd(request: WelchRequest):
    return {"result": get_welch_method().psd(request.signal, request.nperseg)}
