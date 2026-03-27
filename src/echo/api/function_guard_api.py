"""函数守卫API"""

from fastapi import APIRouter

from echo.research.function_guard import get_function_guard


router = APIRouter(prefix="/api/function-guard", tags=["function-guard"])


@router.post("/guard")
async def guard():
    return {"result": None}
