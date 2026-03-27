"""Z变换API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/z-transform", tags=["z-transform"])


@router.post("/transform")
async def transform():
    return {"result": None}
