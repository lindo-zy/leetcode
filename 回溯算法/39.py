#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrace(nums, target, tmp):
            if target == 0:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] <= target:
                    backtrace(nums[i:], target - nums[i], tmp + [nums[i]])

        backtrace(candidates, target, [])
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(s.combinationSum(candidates, target))
