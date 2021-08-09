#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        slow = list1
        fast = list1
        while a - 1:
            slow = slow.next
            a -= 1
        while b + 1:
            fast = fast.next
            b -= 1
        tail = list2
        while tail.next:
            tail = tail.next
        slow.next = list2
        tail.next = fast
        return list1


if __name__ == '__main__':
    s = Solution()
    list1 = [0, 1, 2, 3, 4, 5]
    a = 3
    b = 4
    list2 = [1000000, 1000001, 1000002]
    from gen_node import gen_node

    print(s.mergeInBetween(gen_node(list1), a, b, gen_node(list2)))
