#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # i-j<=k
        res = 0
        cur = 0


if __name__ == '__main__':
    s = Solution()
    nums = [10, 2, -10, 5, 20]
    k = 2
    print(s.constrainedSubsetSum(nums, k))
