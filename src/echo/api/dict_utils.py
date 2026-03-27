"""字典工具API"""

from fastapi import APIRouter

from echo.research.dict_utils import get_dict_utils


router = APIRouter(prefix="/api/dict", tags=["dict"])


@router.post("/get_nested")
async def get_nested(data: dict, path: str, default: str = None):
    return {"result": get_dict_utils().get_nested(data, path, default)}


@router.post("/set_nested")
async def set_nested(data: dict, path: str, value: str):
    return {"result": get_dict_utils().set_nested(data, path, value)}


@router.post("/flatten")
async def flatten(data: dict, prefix: str = ""):
    return {"result": get_dict_utils().flatten(data, prefix)}