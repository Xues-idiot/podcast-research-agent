"""默认值处理API"""

from fastapi import APIRouter

from echo.research.defaults_handler import get_defaults_handler


router = APIRouter(prefix="/api/defaults-handler", tags=["defaults-handler"])


@router.post("/default")
async def default(value, default_val):
    return {"result": get_defaults_handler().default(value, default_val)}