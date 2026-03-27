"""过零检测API"""

from fastapi import APIRouter

from echo.research.zero_crossing import get_zero_crossing


router = APIRouter(prefix="/api/zero-crossing", tags=["zero-crossing"])


@router.post("/find")
async def find(signal: list):
    return {"result": get_zero_crossing().find_crossings(signal)}
