#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1]
    print(s.nextGreaterElements(nums))
