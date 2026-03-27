"""窗函数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.window_function import get_window_function


router = APIRouter(prefix="/api/window", tags=["window"])


class WindowRequest(BaseModel):
    n: int


@router.post("/hamming")
async def hamming(request: WindowRequest):
    return {"result": get_window_function().hamming(request.n)}
