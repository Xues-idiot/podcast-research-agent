"""防抖调用API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.debounce_call import get_debounce_call_tool


router = APIRouter(prefix="/api/debounce-call", tags=["debounce-call"])


class DebounceRequest(BaseModel):
    delay: float


@router.post("/debounce")
async def debounce(request: DebounceRequest):
    tool = get_debounce_call_tool()
    return {"message": "Debounce configured", "delay": request.delay}