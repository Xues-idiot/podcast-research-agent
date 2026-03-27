"""差分API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.difference_tool import get_difference_tool


router = APIRouter(prefix="/api/difference", tags=["difference"])


class DiffRequest(BaseModel):
    data: list
    periods: int = 1


@router.post("/diff")
async def diff(request: DiffRequest):
    return {"result": get_difference_tool().diff(request.data, request.periods)}
