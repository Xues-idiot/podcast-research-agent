"""INI解析器API"""

from fastapi import APIRouter

from echo.research.ini_parser import get_ini_parser


router = APIRouter(prefix="/api/ini", tags=["ini"])


@router.post("/parse")
async def parse(text: str):
    """解析INI"""
    tool = get_ini_parser()
    return {"result": tool.parse(text)}
