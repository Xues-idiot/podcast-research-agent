"""调用跟踪API"""

from fastapi import APIRouter

from echo.research.call_tracker import get_call_tracker


router = APIRouter(prefix="/api/call-tracker", tags=["call-tracker"])


@router.post("/track")
async def track(func):
    return {"result": get_call_tracker().track(func)}


@router.get("/calls")
async def get_calls():
    return {"result": get_call_tracker().get_calls()}


@router.post("/clear")
async def clear():
    get_call_tracker().clear()
    return {"success": True}