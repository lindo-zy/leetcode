#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        for i in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        p0.next.next = cur
        p0.next = pre

        return dummy.next


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    from gen_node import gen_node

    print(sn.reverseBetween(gen_node(head), left, right))
