"""Slug生成API"""

from fastapi import APIRouter

from echo.research.slug_generator import get_slug_generator


router = APIRouter(prefix="/api/slug", tags=["slug"])


@router.post("/generate")
async def generate_slug(text: str, max_length: int = 50):
    return {"slug": get_slug_generator().generate(text, max_length)}


@router.post("/from_url")
async def from_url(url: str):
    return {"slug": get_slug_generator().generate_from_url(url)}