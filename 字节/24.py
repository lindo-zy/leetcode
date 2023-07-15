# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tmp = head.next

        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp


if __name__ == '__main__':
    sn = Solution()
    head = [1, 2, 3, 4]
    from gen_node import gen_node

    print(sn.swapPairs(gen_node(head)))
