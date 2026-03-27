"""享元工厂API"""

from fastapi import APIRouter

from echo.research.flyweight_tool import get_flyweight_factory


router = APIRouter(prefix="/api/flyweight", tags=["flyweight"])


@router.post("/get")
async def get(key: str, factory):
    return {"result": get_flyweight_factory().get(key, factory)}