"""HTML解析API"""

from fastapi import APIRouter

from echo.research.html_parser import get_html_parser


router = APIRouter(prefix="/api/html", tags=["html"])


@router.post("/extract_text")
async def extract_text(html: str):
    return {"text": get_html_parser().extract_text(html)}


@router.post("/extract_links")
async def extract_links(html: str):
    return {"links": get_html_parser().extract_links(html)}


@router.post("/extract_images")
async def extract_images(html: str):
    return {"images": get_html_parser().extract_images(html)}


@router.post("/strip")
async def strip_tags(html: str):
    return {"text": get_html_parser().strip_tags(html)}