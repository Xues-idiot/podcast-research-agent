"""异常值检测API"""

from fastapi import APIRouter

from echo.research.outlier_detector import get_outlier_detector


router = APIRouter(prefix="/api/outlier", tags=["outlier"])


@router.post("/iqr")
async def iqr(data: list):
    return {"result": get_outlier_detector().iqr_outliers(data)}
