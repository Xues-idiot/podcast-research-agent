"""管道运行器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pipeline_runner import get_pipeline_runner


router = APIRouter(prefix="/api/pipeline", tags=["pipeline"])


class PipelineRequest(BaseModel):
    value: str
    functions: list


@router.post("/pipe")
async def pipe(request: PipelineRequest):
    return {"result": get_pipeline_runner().pipe(request.value)}
