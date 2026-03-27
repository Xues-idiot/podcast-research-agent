"""管道API"""

from fastapi import APIRouter

from echo.research.pipeline_tool import get_pipeline_tool


router = APIRouter(prefix="/api/pipeline", tags=["pipeline"])


@router.post("/pipe")
async def pipe(value, *funcs):
    return {"result": get_pipeline_tool().pipe(value, *funcs)}