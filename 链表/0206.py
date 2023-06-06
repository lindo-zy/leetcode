#!/usr/bin/python3
# -*- coding:utf-8 -*-

# https://leetcode.cn/problems/palindrome-linked-list-lcci/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针
        if not head:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = slow
        while slow and slow.next:
            tmp = slow.next.next
            slow.next.next = pre
            pre = slow.next
            slow.next = tmp
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True


if __name__ == '__main__':
    pass
