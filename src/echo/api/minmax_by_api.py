"""最小最大API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.minmax_by import get_minmax_by


router = APIRouter(prefix="/api/minmax-by", tags=["minmax-by"])


class MinMaxByRequest(BaseModel):
    items: list
    key_func: str = None


@router.post("/min")
async def min_by(request: MinMaxByRequest):
    key_func = eval(request.key_func) if request.key_func else None
    return {"result": get_minmax_by().min_by(request.items, key_func)}


@router.post("/max")
async def max_by(request: MinMaxByRequest):
    key_func = eval(request.key_func) if request.key_func else None
    return {"result": get_minmax_by().max_by(request.items, key_func)}
