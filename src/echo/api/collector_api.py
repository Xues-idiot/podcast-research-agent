"""收集器API"""

from fastapi import APIRouter

from echo.research.collector_tool import get_collector_tool


router = APIRouter(prefix="/api/collector", tags=["collector"])


@router.post("/collect")
async def collect(items: list, condition=None):
    return {"result": get_collector_tool().collect(items, condition)}