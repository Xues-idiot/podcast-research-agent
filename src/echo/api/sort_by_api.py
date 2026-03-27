"""排序API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.sort_by import get_sort_by


router = APIRouter(prefix="/api/sort-by", tags=["sort-by"])


class SortByRequest(BaseModel):
    items: list
    key_func: str = None
    reverse: bool = False


@router.post("/sort")
async def sort(request: SortByRequest):
    key_func = eval(request.key_func) if request.key_func else None
    return {"result": get_sort_by().sort_by(request.items, key_func, request.reverse)}
