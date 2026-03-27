"""深拷贝API"""

from fastapi import APIRouter

from echo.research.deepcopy_tool import get_deepcopy_tool


router = APIRouter(prefix="/api/deepcopy", tags=["deepcopy"])


@router.post("/deepcopy")
async def deepcopy(obj):
    return {"result": get_deepcopy_tool().deepcopy(obj)}