"""Lomb-Scargle API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.Lomb_scargle import get_lomb_scargle


router = APIRouter(prefix="/api/lomb-scargle", tags=["lomb-scargle"])


class LSRequest(BaseModel):
    t: list
    y: list
    frequencies: list


@router.post("/periodogram")
async def periodogram(request: LSRequest):
    return {"result": get_lomb_scargle().periodogram(request.t, request.y, request.frequencies)}
