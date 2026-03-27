"""字典查询API"""

from fastapi import APIRouter

from echo.research.dict_query import get_dict_query


router = APIRouter(prefix="/api/dict-query", tags=["dict-query"])


@router.get("/has-key")
async def has_key(data: dict, key: str):
    return {"result": get_dict_query().has_key(data, key)}


@router.get("/keys")
async def get_keys(data: dict):
    return {"result": get_dict_query().get_keys(data)}


@router.get("/values")
async def get_values(data: dict):
    return {"result": get_dict_query().get_values(data)}