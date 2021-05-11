#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) == x:
            return len(nums)
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
        t = sum(nums) - x
        res = float('-inf')
        ds = {}
        for index, num in enumerate(pre):
            if num - t in ds:
                res = max(res, index - ds[num - t])
            if num not in ds:
                ds[num] = index
        return len(nums) - res if res != float('-inf') else -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    print(s.minOperations(nums, x))
