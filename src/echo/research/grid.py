"""网格工具"""

from typing import Optional, Any


class GridTool:
    """网格工具"""

    def make_grid(self, rows: int, cols: int, default: Any = None) -> list:
        """创建网格"""
        return [[default for _ in range(cols)] for _ in range(rows)]

    def get_cell(self, grid: list, row: int, col: int, default: Any = None) -> Any:
        """获取单元格"""
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            return grid[row][col]
        return default


_tool: Optional[GridTool] = None


def get_grid_tool() -> GridTool:
    global _tool
    if _tool is None:
        grid_tool = GridTool()
    return grid_tool