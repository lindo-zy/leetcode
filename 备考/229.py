#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        for i, j in groupby(nums):
            if len(list(j)) > n // 3:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print(s.majorityElement(nums))
