#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        m = int((sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums))))
        # n为重复的数

        for i in range(1, len(nums) + 1):
            if i not in nums:
                return [m, i]


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 2, 2, 4]
    nums = [2, 2]
    # nums = [3, 2, 3, 4, 6, 5]
    print(s.findErrorNums(nums))
