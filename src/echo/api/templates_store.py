"""模板API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.templates_store import ResearchTemplate, get_template_store


router = APIRouter(prefix="/api/templates", tags=["templates"])


class AddTemplateRequest(BaseModel):
    id: str
    name: str
    description: str
    steps: list = []
    config: dict = {}


@router.get("/")
async def list_templates():
    store = get_template_store()
    templates = store.list_all()
    return {"templates": [t.__dict__ for t in templates], "count": len(templates)}


@router.get("/{template_id}")
async def get_template(template_id: str):
    store = get_template_store()
    template = store.get(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template.__dict__


@router.post("/")
async def add_template(request: AddTemplateRequest):
    store = get_template_store()
    template = ResearchTemplate(
        id=request.id,
        name=request.name,
        description=request.description,
        steps=request.steps,
        config=request.config,
    )
    if not store.add(template):
        raise HTTPException(status_code=400, detail="Template already exists")
    return template.__dict__


@router.delete("/{template_id}")
async def remove_template(template_id: str):
    store = get_template_store()
    if not store.remove(template_id):
        raise HTTPException(status_code=404, detail="Template not found or cannot be removed")
    return {"status": "removed"}
