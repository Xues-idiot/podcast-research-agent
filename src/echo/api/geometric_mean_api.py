"""几何平均API"""

from fastapi import APIRouter

from echo.research.geometric_mean import get_geometric_mean


router = APIRouter(prefix="/api/geometric-mean", tags=["geometric-mean"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_geometric_mean().geometric_mean(data)}
