#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        ans = n + 1
        total = 0
        while right < n:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    sn = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(sn.minSubArrayLen(target, nums))
