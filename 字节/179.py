#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Cmp(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=Cmp, reverse=True)
        return str(int(''.join(nums)))


if __name__ == '__main__':
    sn = Solution()
    nums = [10, 2]
    nums = [3, 30, 34, 5, 9]
    print(sn.largestNumber(nums))
