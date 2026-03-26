"""自动保存API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.watchdog import get_autosave


router = APIRouter(prefix="/api/autosave", tags=["autosave"])


class SaveDraftRequest(BaseModel):
    research_id: str
    data: dict


@router.post("/")
async def save_draft(request: SaveDraftRequest):
    autosave = get_autosave()
    autosave.save_draft(request.research_id, request.data)
    return {"status": "saved", "research_id": request.research_id}


@router.get("/{research_id}")
async def get_draft(research_id: str):
    autosave = get_autosave()
    draft = autosave.get_draft(research_id)
    if not draft:
        raise HTTPException(status_code=404, detail="Draft not found")
    return {"research_id": research_id, "data": draft}


@router.delete("/{research_id}")
async def delete_draft(research_id: str):
    autosave = get_autosave()
    if not autosave.delete_draft(research_id):
        raise HTTPException(status_code=404, detail="Draft not found")
    return {"status": "deleted"}


@router.get("/")
async def list_drafts():
    autosave = get_autosave()
    return {"drafts": autosave.list_drafts()}
