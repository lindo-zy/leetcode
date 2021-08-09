#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        vals, stack = [], [0]

        while head:
            vals.append(head.val)
            head = head.next
        # 找到下一个比他大的节点

        for i in range(len(vals) - 1, -1, -1):
            while stack[-1] and vals[i] >= stack[-1]:
                stack.pop()
            stack.append(vals[i])
            vals[i] = stack[-2]
        return vals


if __name__ == '__main__':
    s = Solution()
    head = [2, 7, 4, 3, 5]
    from gen_node import gen_node

    print(s.nextLargerNodes(gen_node(head)))
