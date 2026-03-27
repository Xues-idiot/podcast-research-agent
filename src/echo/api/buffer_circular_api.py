"""循环缓冲API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.buffer_circular import get_buffer_circular


router = APIRouter(prefix="/api/buffer-circular", tags=["buffer-circular"])


class BufferRequest(BaseModel):
    item: str


@router.post("/write")
async def write(request: BufferRequest):
    get_buffer_circular().write(request.item)
    return {"success": True}


@router.post("/read")
async def read():
    return {"result": get_buffer_circular().read()}
