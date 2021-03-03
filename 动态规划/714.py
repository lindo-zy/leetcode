#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)

        dp = [0, -prices[0]]

        for i in range(1, size):
            # 其中 dp[1] 需要用到前一天 dp[0] 的值，但 dp[0] 会先变化，这里 tmp 先进行暂存
            tmp = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], tmp - prices[i])

        return dp[0]


if __name__ == '__main__':
    sn = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2  # 8
    print(sn.maxProfit(prices, fee))
