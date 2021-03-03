#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 0  # 买
        dp[0][1] = -prices[0] - fee  # 卖
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        print(dp)
        return dp[-1][0]

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        profit0 = 0
        profit1 = -prices[0] - fee
        for i in range(1, n):
            new_profit0 = max(profit0, profit1 + prices[i])
            new_profit1 = max(profit1, profit0 - prices[i] - fee)
            profit0 = new_profit0
            profit1 = new_profit1
        return profit0

    def maxProfit3(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[j] 表示 [0, i] 区间内，到第 i 天（从 0 开始）状态为 j 时的最大收益
        # j = 0 表示不持股，j = 1 表示持股
        # 并且规定在买入股票的时候，扣除手续费

        dp = [0, 0]  #
        dp[0] = 0
        dp[1] = -prices[0] - fee
        for i in range(1, n):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[0] - prices[i] - fee)

        return dp[0]


if __name__ == '__main__':
    s = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2  # 8
    print(s.maxProfit(prices, fee))
    print(s.maxProfit2(prices, fee))
    print(s.maxProfit3(prices, fee))
