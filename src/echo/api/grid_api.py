"""网格工具API"""

from fastapi import APIRouter

from echo.research.grid import get_grid_tool


router = APIRouter(prefix="/api/grid", tags=["grid"])


@router.post("/make")
async def make_grid(rows: int, cols: int, default=None):
    return {"result": get_grid_tool().make_grid(rows, cols, default)}


@router.get("/cell")
async def get_cell(grid: list, row: int, col: int, default=None):
    return {"value": get_grid_tool().get_cell(grid, row, col, default)}