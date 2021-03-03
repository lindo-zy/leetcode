#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], (i >= 2 if dp[i - 2][0] else 0) - prices[i])

        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        prevProfit0 = 0
        Profit0 = 0
        Profit1 = -prices[0]
        for i in range(1, n):
            nextProfit0 = max(Profit0, Profit1 + prices[i])
            nextProfit1 = max(Profit1, prevProfit0 - prices[i])
            prevProfit0 = Profit0
            Profit0 = nextProfit0
            Profit1 = nextProfit1
        return Profit0


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 0, 2]  # 3
    print(s.maxProfit(prices))
    print(s.maxProfit2(prices))
