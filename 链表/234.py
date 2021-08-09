#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        seen = []
        while head:
            seen.append(head.val)
            head = head.next
        if seen == seen[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 2, 1]
    from gen_node import gen_node

    print(s.isPalindrome(gen_node(head)))
