"""隐马尔可夫API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/hmm", tags=["hmm"])


@router.post("/forward")
async def forward():
    return {"result": None}
