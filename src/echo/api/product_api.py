"""乘积API"""

from fastapi import APIRouter

from echo.research.product_tool import get_product_tool


router = APIRouter(prefix="/api/product", tags=["product"])


@router.post("/product")
async def product(items: list):
    return {"result": get_product_tool().product(items)}