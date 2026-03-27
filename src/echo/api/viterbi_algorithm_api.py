"""维特比算法API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/viterbi", tags=["viterbi"])


@router.post("/decode")
async def decode():
    return {"result": None}
