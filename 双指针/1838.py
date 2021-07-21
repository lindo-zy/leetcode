#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 1
        j = 0
        window_sum = 0
        for i in range(n):
            window_sum += (nums[i] - nums[i - 1]) * (i - j)
            while window_sum > k:
                window_sum -= nums[i] - nums[j]
                j += 1
            ans = max(i - j + 1, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 8, 13]
    k = 5
    print(s.maxFrequency(nums, k))
