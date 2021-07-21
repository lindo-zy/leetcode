#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return 0 if sum(map(int, ''.join(str(min(nums))))) % 2 else 1


if __name__ == '__main__':
    s = Solution()
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    # nums = [99, 77, 33, 66, 55]
    print(s.sumOfDigits(nums))
