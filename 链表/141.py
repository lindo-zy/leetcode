#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast = head
        slow = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

        # 解法2
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False


if __name__ == '__main__':
    from gen_node import ListNode

    s = Solution()
    head = [3, 2, 0, -4]
    pos = 1
    node = ListNode(head)
    print(s.hasCycle(node))
