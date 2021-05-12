#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrace(start, tmp):
            res.append(tmp)
            for i in range(start, n):
                backtrace(i + 1, tmp + [nums[i]])

        backtrace(0, [])

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
