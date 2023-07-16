#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in dt:
                return [dt[target - nums[i]], i]
            dt[nums[i]] = i
