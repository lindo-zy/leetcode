#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        tmp = ret = ListNode()
        while head:
            if head.val != val:
                tmp.next = head
                tmp = tmp.next
            head = head.next
        tmp.next = None
        return ret.next


if __name__ == '__main__':
    s = Solution()
    from gen_node import gen_node

    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    print(s.removeElements(gen_node(head), val))
