#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = dp[i] + dp[i - c]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(s.change(amount, coins))
