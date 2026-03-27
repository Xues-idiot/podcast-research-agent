"""空操作API"""

from fastapi import APIRouter

from echo.research.noop_func import get_noop_func


router = APIRouter(prefix="/api/noop", tags=["noop"])


@router.post("/noop")
async def noop():
    get_noop_func().noop()
    return {"success": True}
