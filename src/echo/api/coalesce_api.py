"""合并API"""

from fastapi import APIRouter

from echo.research.coalesce_tool import get_coalesce_tool


router = APIRouter(prefix="/api/coalesce", tags=["coalesce"])


@router.post("/coalesce")
async def coalesce(*values):
    return {"result": get_coalesce_tool().coalesce(*values)}