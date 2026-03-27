"""粒子滤波API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/particle-filter", tags=["particle-filter"])


@router.post("/filter")
async def filter():
    return {"result": None}
