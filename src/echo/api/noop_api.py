"""空操作API"""

from fastapi import APIRouter

from echo.research.noop_tool import get_noop_tool


router = APIRouter(prefix="/api/noop", tags=["noop"])


@router.post("/noop")
async def noop(*args, **kwargs):
    get_noop_tool().noop(*args, **kwargs)
    return {"success": True}