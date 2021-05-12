#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrace(start, tmp):
            if len(tmp) >= 2:
                if tmp[-1] >= tmp[-2]:
                    res.append(tmp)
                else:
                    return
            for i in range(start, n):
                if nums[i] in nums[start:i]:
                    continue
                backtrace(i + 1, tmp + [nums[i]])

        backtrace(0, [])

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [4, 6, 7, 7]
    nums = [4, 4, 3, 2, 1]
    print(s.findSubsequences(nums))
