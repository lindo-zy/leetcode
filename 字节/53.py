#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # 转移方程，加不加上一次的结果
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
