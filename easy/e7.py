#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        result = temp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l1, temp.next = l1.next, l1
            else:
                l2, temp.next = l2.next, l2
            temp = temp.next
        temp.next = l1 or l2
        print(result)
        return result.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l1 = ListNode(1)
    l1.next = ListNode(2)
    print(l1.val)
    print(l1.next.val)

    # l2 = ListNode([1, 3, 4])
    # s = Solution()
    # result = s.mergeTwoLists(l1, l2)
