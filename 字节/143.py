#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middle(head)
        h = self.reverse(mid)
        # 这个地方要画图，交替穿插的
        while h.next:
            tmp = head.next
            tmp2 = h.next
            
            head.next = h
            h.next = tmp

            head = tmp
            h = tmp2

    def middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 4]
    from gen_node import gen_node

    print(sn.reorderList(gen_node(head)))
