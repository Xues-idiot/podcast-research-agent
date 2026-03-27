"""扫描累加器API"""

from fastapi import APIRouter

from echo.research.scan_accumulator import get_scan_accumulator


router = APIRouter(prefix="/api/scan", tags=["scan"])


@router.post("/scan")
async def scan_items():
    tool = get_scan_accumulator()
    return {"success": True}
