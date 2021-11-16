#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        self.res = []
        candidates.sort()

        def dfs(target, tmp, start):
            if target == 0:
                self.res.append(tmp)
                return

            for i in range(start, n):
                if target - candidates[i] >= 0:
                    dfs(target - candidates[i], tmp + [candidates[i]], i)

        dfs(target, [], 0)
        return self.res


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7

    candidates = [2, 3, 5]
    target = 8
    print(s.combinationSum(candidates, target))
