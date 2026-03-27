"""距离计算API"""

from fastapi import APIRouter

from echo.research.distance_calculator import get_distance_calculator


router = APIRouter(prefix="/api/distance", tags=["distance"])


@router.post("/euclidean")
async def euclidean(x1: float, y1: float, x2: float, y2: float):
    return {"result": get_distance_calculator().euclidean(x1, y1, x2, y2)}


@router.post("/manhattan")
async def manhattan(x1: float, y1: float, x2: float, y2: float):
    return {"result": get_distance_calculator().manhattan(x1, y1, x2, y2)}


@router.post("/haversine")
async def haversine(lat1: float, lon1: float, lat2: float, lon2: float):
    return {"result": round(get_distance_calculator().haversine(lat1, lon1, lat2, lon2), 2)}