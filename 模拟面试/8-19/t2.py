#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # 速度和*效率中的最小值->和越大*效率的最小值最大
        arr = []
        for i in zip(speed, efficiency):
            arr.append(i)
        # 按最大效率排序
        arr.sort(key=lambda x: x[1], reverse=True)
        print(arr)
        total = 0
        ans = 0
        speed_heap = []
        for s, e in arr:
            heapq.heappush(speed_heap, s)
            if len(speed_heap) > k:
                total -= heapq.heappop(speed_heap)
            total += s
            ans = max(ans, e * total)
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    # n = 6
    # speed = [2, 10, 3, 1, 5, 8]
    # efficiency = [5, 4, 3, 9, 7, 2]
    # k = 2

    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 4

    # n = 6
    # speed = [2, 10, 3, 1, 5, 8]
    # efficiency = [5, 4, 3, 9, 7, 2]
    # k = 2
    print(s.maxPerformance(n, speed, efficiency, k))
