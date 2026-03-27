"""字典访问API"""

from fastapi import APIRouter

from echo.research.dict_accessor import get_dict_accessor


router = APIRouter(prefix="/api/dict-accessor", tags=["dict-accessor"])


@router.get("/get")
async def get_value(data: dict, key: str, default=None):
    return {"value": get_dict_accessor().get_value(data, key, default)}


@router.get("/safe-get")
async def safe_get(data: dict, key: str):
    return {"value": get_dict_accessor().safe_get(data, key)}