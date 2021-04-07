#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # n = len(stones)
        # dp = []  # 初始状态
        # for i in range(n):
        #     for j in range(1, i):
        #         if stones[i] < stones[j]:
        #             dp[i][j] = dp[i][j]
        #         if stones[i] == stones[j]:
        #             dp[i][j] = 0
        #
        # return dp

        if not stones:
            return 0
        n = len(stones)
        s = sum(stones)
        dp = [0] * (s // 2 + 1)

        for k in range(n):
            for i in range(s // 2, stones[k] - 1, -1):
                dp[i] = max(dp[i], dp[i - stones[k]] + stones[k])

        return s - 2 * dp[-1]


if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]  # 1
    print(s.lastStoneWeightII(stones))
