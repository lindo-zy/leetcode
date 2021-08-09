#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == '__main__':
    s = Solution()
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]
    skipA = 2
    skipB = 3
    from gen_node import ListNode

    print(s.getIntersectionNode(ListNode(listA), ListNode(listB)))
