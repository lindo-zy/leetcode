#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        # 建dp空间
        dp = [[0] * i for i in range(1, n + 1)]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for k in range(i + 1):
                if k == 0:
                    dp[i][k] = dp[i - 1][k] + triangle[i][k]
                elif k == i:
                    dp[i][k] = dp[i - 1][k - 1] + triangle[i][k]
                else:
                    dp[i][k] = min(dp[i - 1][k - 1], dp[i - 1][k]) + triangle[i][k]

        return min(dp[-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]  # 11
    sn = Solution()
    print(sn.minimumTotal(triangle))
