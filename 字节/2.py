from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        p = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y

            if s >= 10:
                p.next = ListNode(s - 10)
                carry = 1
            else:
                p.next = ListNode(s)
                carry = 0
            p = p.next
            l1 = l1.next
            l2 = l2.next
        if carry:
            p.next = ListNode(carry)

        return dummy.next
