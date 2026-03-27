"""Slugify API"""

from fastapi import APIRouter

from echo.research.slugify import get_slugify


router = APIRouter(prefix="/api/slugify", tags=["slugify"])


@router.post("/slugify")
async def slugify(text: str):
    """Slug化"""
    tool = get_slugify()
    return {"result": tool.slugify(text)}
