"""迭代器遍历器API"""

from fastapi import APIRouter

from echo.research.iterator_walker import get_iterator_walker


router = APIRouter(prefix="/api/iterator-walker", tags=["iterator-walker"])


@router.post("/walk")
async def walk_iterator():
    walker = get_iterator_walker()
    return {"success": True}
