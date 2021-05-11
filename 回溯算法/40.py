#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrace(start, target, tmp):
            if target == 0:
                res.append(tmp[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrace(i + 1, target - candidates[i], tmp + [candidates[i]])

        backtrace(0, target, [])
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))
