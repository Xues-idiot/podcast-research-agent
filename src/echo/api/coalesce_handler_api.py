"""合并处理API"""

from fastapi import APIRouter

from echo.research.coalesce_handler import get_coalesce_handler


router = APIRouter(prefix="/api/coalesce-handler", tags=["coalesce-handler"])


@router.post("/coalesce")
async def coalesce(*values):
    return {"result": get_coalesce_handler().coalesce(*values)}