#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(s.findPeakElement(nums))
