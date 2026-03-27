"""XML格式化API"""

from fastapi import APIRouter

from echo.research.xml_formatter import get_xml_formatter


router = APIRouter(prefix="/api/xml", tags=["xml"])


@router.post("/format")
async def format_xml(xml_str: str, indent: str = "  "):
    return {"result": get_xml_formatter().format(xml_str, indent)}


@router.post("/minify")
async def minify_xml(xml_str: str):
    return {"result": get_xml_formatter().minify(xml_str)}