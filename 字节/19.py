#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    from gen_node import gen_node

    print(sn.removeNthFromEnd(gen_node(head), n))
