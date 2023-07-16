#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            # 判断是否是第一个数字
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res
