"""观察者API"""

from fastapi import APIRouter

from echo.research.observer_tool import get_observer


router = APIRouter(prefix="/api/observer", tags=["observer"])


@router.post("/attach")
async def attach(handler):
    get_observer().attach(handler)
    return {"success": True}


@router.post("/notify")
async def notify(*args, **kwargs):
    get_observer().notify(*args, **kwargs)
    return {"success": True}