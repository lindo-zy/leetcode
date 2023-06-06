#!/usr/bin/python3
# -*- coding:utf-8 -*-
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针,快的比慢的多走一步
        if not head:
            return head
        slow, fast = head, head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return head


if __name__ == '__main__':
    from gen_node import gen_node

    head = gen_node([1, 1, 2, 3, 3])
    s = Solution()
    r = s.deleteDuplicates(head)
    print(r)
