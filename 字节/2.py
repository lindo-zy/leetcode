#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


if __name__ == '__main__':
    sn = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    from gen_node import gen_node

    print(sn.addTwoNumbers(gen_node(l1), gen_node(l2)))
