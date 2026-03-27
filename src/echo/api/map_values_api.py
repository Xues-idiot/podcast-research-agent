"""映射值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.map_values import get_map_values


router = APIRouter(prefix="/api/map-values", tags=["map-values"])


class MapValuesRequest(BaseModel):
    items: list
    func: str = "lambda x: x"


@router.post("/map")
async def map_values(request: MapValuesRequest):
    func = eval(request.func)
    return {"result": get_map_values().map_values(request.items, func)}
