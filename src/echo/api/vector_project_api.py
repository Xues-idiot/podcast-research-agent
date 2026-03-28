"""向量投影API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_project import get_vector_project_tool


router = APIRouter(prefix="/api/vector-project", tags=["vector-project"])


class ProjectRequest(BaseModel):
    a: list[float]
    b: list[float]


@router.post("/project")
async def project(request: ProjectRequest):
    tool = get_vector_project_tool()
    return {"result": tool.project(request.a, request.b)}