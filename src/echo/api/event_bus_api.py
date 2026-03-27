"""事件总线API"""

from fastapi import APIRouter

from echo.research.event_bus import get_event_bus


router = APIRouter(prefix="/api/event-bus", tags=["event-bus"])


@router.post("/subscribe")
async def subscribe(event: str, handler):
    get_event_bus().subscribe(event, handler)
    return {"success": True}


@router.post("/publish")
async def publish(event: str):
    get_event_bus().publish(event)
    return {"success": True}