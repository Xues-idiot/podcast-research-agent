"""环形缓冲区API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.ring_buffer import get_ring_buffer


router = APIRouter(prefix="/api/ring-buffer", tags=["ring-buffer"])


class RingRequest(BaseModel):
    item: Any


@router.post("/push")
async def push(request: RingRequest):
    get_ring_buffer().push(request.item)
    return {"success": True}


@router.post("/get-all")
async def get_all():
    return {"result": get_ring_buffer().get_all()}
