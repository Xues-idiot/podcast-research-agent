"""字符串构建API"""

from fastapi import APIRouter

from echo.research.stringer import get_stringer


router = APIRouter(prefix="/api/stringer", tags=["stringer"])


@router.post("/build")
async def build(*parts):
    return {"result": get_stringer().build(*parts)}