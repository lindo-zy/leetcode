#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrace(nums, tmp):
            if len(tmp) == n:
                res.append(tmp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrace(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    nums = [1, 2, 3]
    print(s.permuteUnique(nums))
