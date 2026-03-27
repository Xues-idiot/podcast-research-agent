"""聚合API"""

from fastapi import APIRouter

from echo.research.aggregator_tool import get_aggregator_tool


router = APIRouter(prefix="/api/aggregator", tags=["aggregator"])


@router.post("/aggregate")
async def aggregate(items: list, key: str):
    return {"result": get_aggregator_tool().aggregate(items, key)}