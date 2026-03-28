"""模板渲染API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, List

from echo.research.template_render import get_template_render_tool


router = APIRouter(prefix="/api/template-render", tags=["template-render"])


class RenderRequest(BaseModel):
    template: str
    variables: Dict[str, Any]


@router.post("/render")
async def render(request: RenderRequest):
    tool = get_template_render_tool()
    return {"result": tool.render(request.template, request.variables)}


class RenderListRequest(BaseModel):
    template: str
    items: List[Any]
    item_var: str = "item"


@router.post("/render-list")
async def render_list(request: RenderListRequest):
    tool = get_template_render_tool()
    return {"result": tool.render_list(request.template, request.items, request.item_var)}