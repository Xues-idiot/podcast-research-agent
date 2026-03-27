"""模板引擎API"""

from fastapi import APIRouter

from echo.research.template_engine import get_template_engine


router = APIRouter(prefix="/api/template", tags=["template"])


@router.post("/render")
async def render(template: str, context: dict):
    """渲染模板"""
    tool = get_template_engine()
    return {"result": tool.render(template, context)}
