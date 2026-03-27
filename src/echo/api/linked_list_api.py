"""链表API"""

from fastapi import APIRouter

from echo.research.linked_list import get_linked_list_tool, ListNode


router = APIRouter(prefix="/api/linked-list", tags=["linked-list"])


@router.post("/to-list")
async def to_list(values: list):
    """链表转列表"""
    tool = get_linked_list_tool()
    head = None
    for val in values:
        node = tool.create_node(val)
        head = tool.append(head, node)
    return {"list": tool.to_list(head)}
