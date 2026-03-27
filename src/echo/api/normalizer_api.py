"""归一化API"""

from fastapi import APIRouter

from echo.research.normalizer import get_normalizer


router = APIRouter(prefix="/api/normalizer", tags=["normalizer"])


@router.post("/normalize")
async def normalize(data: list):
    return {"result": get_normalizer().normalize(data)}
