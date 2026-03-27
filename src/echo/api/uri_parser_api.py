"""URI解析器API"""

from fastapi import APIRouter

from echo.research.uri_parser import get_uri_parser


router = APIRouter(prefix="/api/uri", tags=["uri"])


@router.post("/parse")
async def parse(uri: str):
    """解析URI"""
    tool = get_uri_parser()
    return {"result": tool.parse(uri)}


@router.post("/build")
async def build(scheme: str, host: str, path: str = "", port: int = None):
    """构建URI"""
    tool = get_uri_parser()
    return {"uri": tool.build(scheme, host, path, port)}
