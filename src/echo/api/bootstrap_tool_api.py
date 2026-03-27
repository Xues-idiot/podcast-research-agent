"""Bootstrap API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.bootstrap_tool import get_bootstrap_tool


router = APIRouter(prefix="/api/bootstrap", tags=["bootstrap"])


class BootstrapRequest(BaseModel):
    data: list
    n_iterations: int = 1000


@router.post("/means")
async def means(request: BootstrapRequest):
    return {"result": get_bootstrap_tool().bootstrap_mean(request.data, request.n_iterations)}
