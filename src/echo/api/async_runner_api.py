"""异步运行器API"""

from fastapi import APIRouter

from echo.research.async_runner import get_async_runner


router = APIRouter(prefix="/api/async-runner", tags=["async-runner"])


@router.post("/run")
async def run():
    return {"result": None}
