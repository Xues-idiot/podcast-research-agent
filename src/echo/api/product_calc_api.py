"""乘积计算API"""

from fastapi import APIRouter

from echo.research.product_calculator import get_product_calculator


router = APIRouter(prefix="/api/product-calc", tags=["product-calc"])


@router.post("/product")
async def product(items: list):
    return {"result": get_product_calculator().product(items)}