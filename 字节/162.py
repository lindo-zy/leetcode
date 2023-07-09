#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sn = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(sn.findPeakElement(nums))
