"""重叠添加API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.overlap_add import get_overlap_add


router = APIRouter(prefix="/api/overlap-add", tags=["overlap-add"])


class OverlapAddRequest(BaseModel):
    frames: list
    hop_size: int


@router.post("/add")
async def add(request: OverlapAddRequest):
    return {"result": get_overlap_add().overlap_add(request.frames, request.hop_size)}
