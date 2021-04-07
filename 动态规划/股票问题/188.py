#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * (2 * k + 1) for i in range(n)]
        for i in range(1, 2 * k + 1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, n):
            for j in range(1, 2 * k + 1):
                if j & 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    k = 2
    prices = [2, 4, 1]
    print(s.maxProfit(k, prices))
