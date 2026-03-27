"""矩API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.moment_tool import get_moment_tool


router = APIRouter(prefix="/api/moment", tags=["moment"])


class MomentRequest(BaseModel):
    data: list
    order: int


@router.post("/raw")
async def raw(request: MomentRequest):
    return {"result": get_moment_tool().raw_moment(request.data, request.order)}
