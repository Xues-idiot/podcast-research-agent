"""过滤API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.filter_by import get_filter_by


router = APIRouter(prefix="/api/filter-by", tags=["filter-by"])


class FilterByRequest(BaseModel):
    items: list
    pred: str = "lambda x: True"


@router.post("/filter")
async def filter(request: FilterByRequest):
    pred = eval(request.pred)
    return {"result": get_filter_by().filter_by(request.items, pred)}
