#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        res = cur / k
        for i in range(k, len(nums)):
            cur = cur - nums[i - k] + nums[i]
            res = max(res, cur / k)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(s.findMaxAverage(nums, k))
