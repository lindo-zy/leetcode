#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    sn = Solution()
    head = [1, 1, 2, 3, 3]
    from gen_node import gen_node

    print(sn.deleteDuplicates(gen_node(head)))
