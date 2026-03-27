"""拉普拉斯变换API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/laplace", tags=["laplace"])


@router.post("/transform")
async def transform():
    return {"result": None}
