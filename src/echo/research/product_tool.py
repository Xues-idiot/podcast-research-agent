"""乘积工具"""

from typing import Optional, List


class ProductTool:
    """乘积工具"""

    def product(self, items: List[float]) -> float:
        """乘积"""
        result = 1
        for item in items:
            result *= item
        return result


_product_tool: Optional[ProductTool] = None


def get_product_tool() -> ProductTool:
    global _product_tool
    if _product_tool is None:
        _product_tool = ProductTool()
    return _product_tool