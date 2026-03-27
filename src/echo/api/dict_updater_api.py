"""字典更新API"""

from fastapi import APIRouter

from echo.research.dict_updater import get_dict_updater


router = APIRouter(prefix="/api/dict-updater", tags=["dict-updater"])


@router.post("/merge")
async def merge_dicts(*dicts: dict):
    return {"result": get_dict_updater().merge_dicts(*dicts)}


@router.post("/update-nested")
async def update_nested(data: dict, updates: dict):
    get_dict_updater().update_nested(data, updates)
    return {"success": True}