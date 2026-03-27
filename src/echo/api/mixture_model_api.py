"""混合模型API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/mixture", tags=["mixture"])


@router.post("/sample")
async def sample():
    return {"result": None}
