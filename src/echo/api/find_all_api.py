"""查找所有API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.find_all import get_find_all


router = APIRouter(prefix="/api/find-all", tags=["find-all"])


class FindAllRequest(BaseModel):
    items: list
    pred: str = "lambda x: True"


@router.post("/find")
async def find(request: FindAllRequest):
    pred = eval(request.pred)
    return {"result": get_find_all().find_all(request.items, pred)}
