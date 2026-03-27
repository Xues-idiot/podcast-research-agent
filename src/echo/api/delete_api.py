"""删除API"""

from fastapi import APIRouter

from echo.research.delete_tool import get_delete_tool


router = APIRouter(prefix="/api/delete", tags=["delete"])


@router.post("/delete")
async def delete(items: list, index: int):
    return {"result": get_delete_tool().delete(items, index)}