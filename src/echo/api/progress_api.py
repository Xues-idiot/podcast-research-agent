"""进度API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.progress import get_progress_tracker


router = APIRouter(prefix="/api/progress", tags=["progress"])


class UpdateProgressRequest(BaseModel):
    research_id: str
    step: str
    percent: float = 0


@router.post("/start/{research_id}")
async def start_progress(research_id: str):
    tracker = get_progress_tracker()
    tracker.start(research_id)
    return {"status": "started", "research_id": research_id}


@router.post("/update")
async def update_progress(request: UpdateProgressRequest):
    tracker = get_progress_tracker()
    tracker.update(request.research_id, request.step, request.percent)
    return {"status": "updated"}


@router.post("/complete/{research_id}")
async def complete_progress(research_id: str):
    tracker = get_progress_tracker()
    tracker.complete(research_id)
    return {"status": "completed"}


@router.get("/{research_id}")
async def get_progress(research_id: str):
    tracker = get_progress_tracker()
    progress = tracker.get(research_id)
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return {"research_id": research_id, **progress}


@router.get("/")
async def list_active():
    tracker = get_progress_tracker()
    return {"active": tracker.list_active()}
