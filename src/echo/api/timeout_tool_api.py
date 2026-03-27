"""超时API"""

from fastapi import APIRouter

from echo.research.timeout import get_timeout


router = APIRouter(prefix="/api/timeout-tool", tags=["timeout-tool"])


@router.post("/timeout")
async def timeout():
    return {"result": None}
