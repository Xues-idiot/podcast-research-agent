"""链表工具"""

from typing import Any, Optional


class ListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedListTool:
    _instance: Optional["LinkedListTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_node(self, value: Any) -> ListNode:
        return ListNode(value)

    def append(self, head: ListNode, node: ListNode) -> ListNode:
        if not head:
            return node
        current = head
        while current.next:
            current = current.next
        current.next = node
        return head

    def to_list(self, head: ListNode) -> List[Any]:
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result


def get_linked_list_tool() -> LinkedListTool:
    return LinkedListTool()
