"""字典转换API"""

from fastapi import APIRouter

from echo.research.dict_transformer import get_dict_transformer


router = APIRouter(prefix="/api/dict-transformer", tags=["dict-transformer"])


@router.post("/map-values")
async def map_values(data: dict, func: str):
    return {"result": get_dict_transformer().map_values(data, eval(func))}


@router.post("/filter-keys")
async def filter_keys(data: dict, func: str):
    return {"result": get_dict_transformer().filter_keys(data, eval(func))}