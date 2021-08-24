#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        a = head
        temp = []
        while a:
            temp.append(a)
            a = a.next

        temp[k - 1], temp[-k] = temp[-k], temp[k - 1]
        for i in range(len(temp) - 1):
            temp[i].next = temp[i + 1]
        temp[-1].next = None
        return temp[0]


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    k = 2
    from gen_node import gen_node

    print(s.swapNodes(gen_node(head), k))
