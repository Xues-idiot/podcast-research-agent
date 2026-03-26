"""导出预设API"""

from fastapi import APIRouter

from echo.research.export_templates import PRESETS


router = APIRouter(prefix="/api/export-presets", tags=["export"])


@router.get("/")
async def list_presets():
    return {"presets": [p.__dict__ for p in PRESETS]}
