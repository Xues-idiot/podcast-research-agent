"""方差分析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.ANOVA_tool import get_anova_tool


router = APIRouter(prefix="/api/anova", tags=["anova"])


class AnovaRequest(BaseModel):
    groups: list


@router.post("/one-way")
async def one_way(request: AnovaRequest):
    return {"result": get_anova_tool().one_way_anova(*request.groups)}
