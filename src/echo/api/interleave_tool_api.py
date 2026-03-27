"""交错工具API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.interleave_tool import get_interleave_tool


router = APIRouter(prefix="/api/interleave", tags=["interleave"])


class InterleaveRequest(BaseModel):
    lists: list


@router.post("/interleave")
async def interleave(request: InterleaveRequest):
    return {"result": get_interleave_tool().interleave(*request.lists)}
