#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 加入第一个窗
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        n = len(nums)
        ans = [-q[0][0]]
        for i in range(k, n):
            # 加入到堆中
            heapq.heappush(q, (-nums[i], i))
            # 判断当前堆顶元素是否在窗中
            while q[0][1] <= i - k:
                # 不在就弹出
                heapq.heappop(q)
            # 取出当前最大值
            ans.append(-q[0][0])
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.maxSlidingWindow(nums, k))
