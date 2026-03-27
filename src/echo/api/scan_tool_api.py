"""扫描工具API"""

from fastapi import APIRouter

from echo.research.scan_tool import get_scan_tool


router = APIRouter(prefix="/api/scan", tags=["scan"])


@router.post("/scan")
async def scan(items: list):
    return {"result": get_scan_tool().scan(items)}
