"""时区转换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.timezone_convert import get_timezone_convert_tool


router = APIRouter(prefix="/api/timezone-convert", tags=["timezone-convert"])


class ConvertRequest(BaseModel):
    time_str: str
    from_tz: str
    to_tz: str


@router.post("/convert")
async def convert(request: ConvertRequest):
    tool = get_timezone_convert_tool()
    return {"result": tool.convert(request.time_str, request.from_tz, request.to_tz)}