"""时间序列API"""

from fastapi import APIRouter

from echo.research.timeseries import get_time_series


router = APIRouter(prefix="/api/timeseries", tags=["timeseries"])


@router.post("/create-series")
async def create_series(points: list):
    """创建时间序列"""
    tool = get_time_series()
    return {"series": tool.create_series(points)}


@router.post("/resample")
async def resample(series: list, interval: int):
    """重采样"""
    tool = get_time_series()
    return {"resampled": tool.resample(series, interval)}
