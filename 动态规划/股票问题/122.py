#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        profit0 = 0
        profit1 = -prices[0]
        for i in range(1, n):
            new_profit0 = max(profit0, profit1 + prices[i])
            new_profit1 = max(profit1, profit0 - prices[i])
            profit0 = new_profit0
            profit1 = new_profit1
        return profit0


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]  # 7
    print(s.maxProfit(prices))
    print(s.maxProfit2(prices))
    print(s.maxProfit3(prices))
