"""乘积计算工具"""

from typing import Optional, List


class ProductCalculator:
    """乘积计算工具"""

    def product(self, items: List[float]) -> float:
        """乘积"""
        result = 1
        for item in items:
            result *= item
        return result


_product_calculator: Optional[ProductCalculator] = None


def get_product_calculator() -> ProductCalculator:
    global _product_calculator
    if _product_calculator is None:
        _product_calculator = ProductCalculator()
    return _product_calculator