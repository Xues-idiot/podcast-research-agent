"""日志API"""

from fastapi import APIRouter

from echo.research.logger_tool import get_logger_tool


router = APIRouter(prefix="/api/logger", tags=["logger"])


@router.post("/log")
async def log(message: str, level: str = "INFO"):
    get_logger_tool().log(message, level)
    return {"success": True}