#!/usr/bin/python3
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, next=head)
        p = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if p.next == cur:
                # 移动
                p = p.next
            else:
                # 跳过重复元素
                p.next = cur.next
            # 移动
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 3, 4, 4, 5]
    from gen_node import gen_node

    print(sn.deleteDuplicates(gen_node(head)))
