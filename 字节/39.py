#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(nums, target, tmp):
            if target == 0:
                res.append(tmp)
            for i in range(len(nums)):
                if nums[i] <= target:
                    dfs(nums[i:], target - nums[i], tmp + [nums[i]])

        dfs(candidates, target, [])

        return res


if __name__ == '__main__':
    sn = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sn.combinationSum(candidates, target))
