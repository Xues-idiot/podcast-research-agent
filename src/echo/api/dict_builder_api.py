"""字典构建API"""

from fastapi import APIRouter

from echo.research.dict_builder import get_dict_builder


router = APIRouter(prefix="/api/dict-builder", tags=["dict-builder"])


@router.post("/build")
async def build_dict(keys: list, values: list):
    return {"result": get_dict_builder().build_dict(keys, values)}


@router.post("/from-items")
async def from_items(items: list):
    return {"result": get_dict_builder().from_items(items)}