"""管道处理API"""

from fastapi import APIRouter

from echo.research.pipeliner import get_pipeliner


router = APIRouter(prefix="/api/pipeliner", tags=["pipeliner"])


@router.post("/pipeline")
async def pipeline(value, *funcs):
    return {"result": get_pipeliner().pipeline(value, *funcs)}