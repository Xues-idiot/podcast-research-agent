"""恒等API"""

from fastapi import APIRouter

from echo.research.identity_tool import get_identity_tool


router = APIRouter(prefix="/api/identity", tags=["identity"])


@router.post("/identity")
async def identity(value):
    return {"result": get_identity_tool().identity(value)}