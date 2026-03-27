"""复制API"""

from fastapi import APIRouter

from echo.research.copy_tool import get_copy_tool


router = APIRouter(prefix="/api/copy", tags=["copy"])


@router.post("/copy")
async def copy(obj):
    return {"result": get_copy_tool().copy(obj)}