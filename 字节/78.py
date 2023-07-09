#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(start, tmp):
            res.append(tmp)
            for i in range(start, n):
                dfs(i + 1, tmp + [nums[i]])

        dfs(0, [])
        return res


if __name__ == '__main__':
    sn = Solution()
    nums = [1, 2, 3]
    print(sn.subsets(nums))
