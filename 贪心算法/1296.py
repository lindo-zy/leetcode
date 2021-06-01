#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 3, 4, 4, 5, 6]  # 1234 3456
    k = 4
    # nums = [1,2,3,4]
    # k = 3
    print(s.isPossibleDivide(nums, k))
