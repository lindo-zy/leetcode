#!/usr/bin/python3
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 3, 4, 4, 5]
    from gen_node import gen_node

    print(sn.deleteDuplicates(gen_node(head)))
