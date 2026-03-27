"""批处理运行器API"""

from fastapi import APIRouter

from echo.research.batch_runner import get_batch_runner


router = APIRouter(prefix="/api/batch-runner", tags=["batch-runner"])


@router.post("/run")
async def run_batch():
    runner = get_batch_runner()
    return {"success": True}
