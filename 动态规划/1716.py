#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    sn = Solution()
    nums = [2, 1, 4, 5, 3, 1, 1, 3]  # 12
    print(sn.massage(nums))
