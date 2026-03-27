"""Baum-Welch API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/baum-welch", tags=["baum-welch"])


@router.post("/train")
async def train():
    return {"result": None}
