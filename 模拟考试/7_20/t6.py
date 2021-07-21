#!/usr/bin/python3
# -*- coding:utf-8 -*-
import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(s.searchInsert(nums, target))
