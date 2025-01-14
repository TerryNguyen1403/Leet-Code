from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        curNode = head

        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode

        return prevNode
