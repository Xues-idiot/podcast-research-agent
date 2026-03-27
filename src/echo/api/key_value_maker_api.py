"""键值工具API"""

from fastapi import APIRouter

from echo.research.key_value_maker import get_key_value_maker


router = APIRouter(prefix="/api/key-value", tags=["key-value"])


@router.post("/make")
async def make_pair(key: str, value: str):
    return {"result": get_key_value_maker().make_pair(key, value)}


@router.post("/from-list")
async def from_list(items: list):
    return {"result": get_key_value_maker().from_list(items)}