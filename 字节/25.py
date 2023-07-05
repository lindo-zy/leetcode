#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        for i in range(k):
            if not p:
                return head
            p = p.next

        pre = None
        cur = head
        while cur != p:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        head.next = self.reverseKGroup(cur, k)

        return pre


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 4, 5]
    k = 2
    from gen_node import gen_node

    print(sn.reverseKGroup(gen_node(head), k))
