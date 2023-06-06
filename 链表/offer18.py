#!/usr/bin/python3
# -*- coding:utf-8 -*-
# https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 快慢指针，快指针指到了指定值时，把下个next挂给slow即可
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next

        return head


if __name__ == '__main__':
    from gen_node import gen_node

    head = gen_node([4, 5, 1, 9])
    val = 5
    s = Solution()
    r = s.deleteNode(head, val)
    print(r)
