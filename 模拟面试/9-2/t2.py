#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        b = nums + nums
        nums.sort()
        for i in range(l):
            a = b[i:i + l]
            if nums == a:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 3, 4]
    print(s.check(nums))
