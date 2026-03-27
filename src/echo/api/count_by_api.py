"""计数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.count_by import get_count_by


router = APIRouter(prefix="/api/count-by", tags=["count-by"])


class CountByRequest(BaseModel):
    items: list
    key_func: str = None


@router.post("/count")
async def count(request: CountByRequest):
    key_func = eval(request.key_func) if request.key_func else None
    return {"result": get_count_by().count_by(request.items, key_func)}
