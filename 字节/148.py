#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import heapq
        p = head
        h = []
        while p:
            heapq.heappush(h, p.val)
            p = p.next

        p = head
        while h:
            p.val = heapq.heappop(h)
            p = p.next
        return head


if __name__ == '__main__':
    sn = Solution()
    head = [4, 2, 1, 3]
    from gen_node import gen_node

    print(sn.sortList(gen_node(head)))
