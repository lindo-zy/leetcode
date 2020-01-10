#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a, b = 1, 2
        for i in range(n - 1):
            a, b = b, a + b
        return a


class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        dp.extend([0] * (n - 2))
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution2()
    n = 8
    print(s.climbStairs(n))
