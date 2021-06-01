#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        dp, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur += num
            if k != 0:
                cur %= k
            pre = dp.setdefault(cur, idx)
            if idx - pre > 1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(s.checkSubarraySum(nums, k))
