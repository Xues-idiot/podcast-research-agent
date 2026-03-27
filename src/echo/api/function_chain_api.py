"""函数链API"""

from fastapi import APIRouter

from echo.research.function_chain import get_function_chain


router = APIRouter(prefix="/api/function-chain", tags=["function-chain"])


@router.post("/add")
async def add(func: str):
    return {"success": True}


@router.post("/execute")
async def execute(value: str):
    return {"result": get_function_chain().execute(value)}
