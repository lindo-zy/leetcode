#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + i)
        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))
