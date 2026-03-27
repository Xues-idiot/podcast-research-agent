"""标准化API"""

from fastapi import APIRouter

from echo.research.standardizer import get_standardizer


router = APIRouter(prefix="/api/standardizer", tags=["standardizer"])


@router.post("/standardize")
async def standardize(data: list):
    return {"result": get_standardizer().standardize(data)}
