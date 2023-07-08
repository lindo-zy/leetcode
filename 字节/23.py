#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 全部取出，再拼接
        import heapq
        dummy = ListNode(0)
        p = dummy
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, idx = heapq.heappop(h)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(h, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


if __name__ == '__main__':
    sn = Solution()

    from gen_node import gen_node

    lists = [gen_node([1, 4, 5]), gen_node([1, 3, 4]), gen_node([2, 6])]

    print(sn.mergeKLists(lists))
