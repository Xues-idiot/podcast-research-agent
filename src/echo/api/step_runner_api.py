"""步骤运行器API"""

from fastapi import APIRouter

from echo.research.step_runner import get_step_runner


router = APIRouter(prefix="/api/step-runner", tags=["step-runner"])


@router.post("/run")
async def run_steps():
    runner = get_step_runner()
    return {"success": True}
