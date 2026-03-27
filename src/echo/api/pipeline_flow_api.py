"""管道API"""

from fastapi import APIRouter

from echo.research.pipeline_flow import get_pipeline_flow


router = APIRouter(prefix="/api/pipeline", tags=["pipeline"])


@router.post("/run")
async def run_pipeline(value: str, funcs: list):
    """运行管道"""
    tool = get_pipeline_flow()
    func_objs = [eval(f) for f in funcs]
    return {"result": tool.pipeline(value, *func_objs)}
