"""管道构建器API"""

from fastapi import APIRouter

from echo.research.pipeline_builder import get_pipeline_builder


router = APIRouter(prefix="/api/pipeline", tags=["pipeline"])


@router.post("/add-step")
async def add_step(func_name: str):
    builder = get_pipeline_builder()
    return {"success": True}


@router.post("/build")
async def build_pipeline():
    builder = get_pipeline_builder()
    pipeline = builder.build()
    return {"success": True}
