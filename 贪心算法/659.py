#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        m = collections.defaultdict(list)
        for x in nums:
            if m.get(x - 1):
                heap = m.get(x - 1)
                ll = heapq.heappop(heap)
                heapq.heappush(m[x], ll + 1)
            else:
                heapq.heappush(m[x], 1)
        return all(not h or h[0] >= 3 for h in m.values())


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 3, 4, 5]
    print(s.isPossible(nums))
