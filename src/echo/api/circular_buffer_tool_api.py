"""环形缓冲区API"""

from fastapi import APIRouter

from echo.research.circular_buffer_tool import get_circular_buffer_tool


router = APIRouter(prefix="/api/circular-buffer", tags=["circular-buffer"])


@router.post("/push")
async def push(item):
    get_circular_buffer_tool().push(item)
    return {"success": True}


@router.get("/get-all")
async def get_all():
    return {"result": get_circular_buffer_tool().get_all()}