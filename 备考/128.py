#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(sorted(nums))


if __name__ == '__main__':
    s = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(s.longestConsecutive(nums))
