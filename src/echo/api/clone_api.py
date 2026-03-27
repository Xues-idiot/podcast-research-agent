"""克隆API"""

from fastapi import APIRouter

from echo.research.clone_tool import get_clone_tool


router = APIRouter(prefix="/api/clone", tags=["clone"])


@router.post("/shallow")
async def shallow_clone(obj):
    return {"result": get_clone_tool().shallow_clone(obj)}


@router.post("/deep")
async def deep_clone(obj):
    return {"result": get_clone_tool().deep_clone(obj)}