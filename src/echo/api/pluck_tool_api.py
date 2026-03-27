"""提取API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pluck_tool import get_pluck_tool


router = APIRouter(prefix="/api/pluck", tags=["pluck"])


class PluckRequest(BaseModel):
    items: list
    key: str


@router.post("/pluck")
async def pluck(request: PluckRequest):
    return {"result": get_pluck_tool().pluck(request.items, request.key)}
