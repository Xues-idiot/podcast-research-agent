"""配置加载API"""

from fastapi import APIRouter

from echo.research.config_loader import get_config_loader


router = APIRouter(prefix="/api/config", tags=["config"])


@router.get("/env")
async def get_env(key: str, default: str = None):
    return {"value": get_config_loader().get_env(key, default)}