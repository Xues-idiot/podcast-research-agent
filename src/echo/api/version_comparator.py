"""版本比较API"""

from fastapi import APIRouter

from echo.research.version_comparator import get_version_comparator


router = APIRouter(prefix="/api/version", tags=["version"])


@router.post("/compare")
async def compare(v1: str, v2: str):
    result = get_version_comparator().compare(v1, v2)
    return {"result": result, "comparison": "less" if result < 0 else "equal" if result == 0 else "greater"}


@router.post("/is_compatible")
async def is_compatible(current: str, required: str):
    return {"compatible": get_version_comparator().is_compatible(current, required)}