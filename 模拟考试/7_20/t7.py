#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = sum(nums)
        n = len(nums)
        s = sum(range(n))
        return cnt - s


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 3, 4, 2]
    nums = [1, 1]
    nums = [2, 2, 2, 2]
    # nums = [1, 1, 2]
    print(s.findDuplicate(nums))
