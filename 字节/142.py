from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dt = set()
        cur = head
        while cur and cur.next:
            if cur in dt:
                return cur
            dt.add(cur)

            cur = cur.next
