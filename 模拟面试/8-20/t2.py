#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        while len(nums) > 0:
            result.append(nums.pop())
            if sum(result) > sum(nums):
                return result


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 7, 6, 7]
    print(s.minSubsequence(nums))
