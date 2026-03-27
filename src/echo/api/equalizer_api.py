"""相等API"""

from fastapi import APIRouter

from echo.research.equalizer import get_equalizer


router = APIRouter(prefix="/api/equalizer", tags=["equalizer"])


@router.post("/equals")
async def equals(a, b):
    return {"result": get_equalizer().equals(a, b)}