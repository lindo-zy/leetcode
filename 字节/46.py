#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(nums, tmp):
            if len(tmp) == n:
                res.append(tmp)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    sn = Solution()
    nums = [1, 2, 3]
    print(sn.permute(nums))
