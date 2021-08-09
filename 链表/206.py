#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    from gen_node import gen_node

    print(s.reverseList(gen_node(head)))
