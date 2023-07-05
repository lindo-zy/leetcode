#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == '__main__':
    sn = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sn.findKthLargest(nums, k))
