#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_heap = []
        min_heap = []
        left = 0
        right = 0
        res = 0
        while right < n:
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))
            # 如果不满足，则left+=1
            if abs(max_heap[0][0] + min_heap[0][0]) > limit:
                if max_heap and max_heap[0][1] <= left:
                    heapq.heappop(max_heap)
                if min_heap and min_heap[0][1] <= left:
                    heapq.heappop(min_heap)
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [8, 2, 4, 7]
    limit = 4

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(s.longestSubarray(nums, limit))
