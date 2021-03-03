#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        buy_in = prices[0]
        for i in range(1, n):
            buy_in = min(buy_in, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - buy_in)
        return dp[-1]

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]  # 初始化dp #dp[0][0]表示卖 dp[0][1]表示买
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        print(dp)
        return dp[-1][0]


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))
    print(s.maxProfit2(prices))
