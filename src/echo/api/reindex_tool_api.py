"""重新索引API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.reindex_tool import get_reindex_tool


router = APIRouter(prefix="/api/reindex", tags=["reindex"])


class ReindexRequest(BaseModel):
    items: list
    start: int = 0


@router.post("/reindex")
async def reindex(request: ReindexRequest):
    return {"result": get_reindex_tool().reindex(request.items, request.start)}
