#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-1,-2,-3]
    # [4, -1, 2, 1]
    result = s.maxSubArray(nums)
    print(result)
