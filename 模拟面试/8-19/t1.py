#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        # 大顶堆
        arr = []
        for i in piles:
            heapq.heappush(arr, -i)
        for i in range(k):
            heapq.heappush(arr, heapq.heappop(arr) // 2)
        return sum([-i for i in arr])


if __name__ == '__main__':
    s = Solution()
    piles = [4, 3, 6, 7]
    k = 3
    print(s.minStoneSum(piles, k))
