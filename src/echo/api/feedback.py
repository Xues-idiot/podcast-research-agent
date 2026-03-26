"""反馈API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.feedback import get_feedback_manager


router = APIRouter(prefix="/api/feedback", tags=["feedback"])


class AddFeedbackRequest(BaseModel):
    type: str
    content: str
    rating: int = 0


class AddBugRequest(BaseModel):
    description: str
    steps: str = ""
    severity: str = "medium"


@router.post("/")
async def add_feedback(request: AddFeedbackRequest):
    manager = get_feedback_manager()
    fb = manager.add_feedback(request.type, request.content, request.rating)
    return fb


@router.get("/")
async def list_feedback():
    manager = get_feedback_manager()
    return {"feedback": manager.list_feedback()}


@router.post("/bugs")
async def add_bug(request: AddBugRequest):
    manager = get_feedback_manager()
    bug = manager.add_bug(request.description, request.steps, request.severity)
    return bug


@router.get("/bugs")
async def list_bugs(status: str = None):
    manager = get_feedback_manager()
    return {"bugs": manager.list_bugs(status=status)}


@router.patch("/bugs/{bug_id}")
async def update_bug_status(bug_id: str, status: str):
    manager = get_feedback_manager()
    if not manager.update_bug_status(bug_id, status):
        raise HTTPException(status_code=404, detail="Bug not found")
    return {"status": "updated"}


@router.get("/stats")
async def get_stats():
    manager = get_feedback_manager()
    return manager.get_stats()
