#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2 for _ in range(n)] for _ in range(n)]

        idx = defaultdict(int)

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                pre = A[i] * 2 - A[j]  # 前一个数 如 3,6构成的数列，前一个数是0=3*2-6
                if pre in idx:
                    dp[i][j] = dp[idx[pre]][i] + 1  # 以 A[i]  A[j]为结尾的等差数组
                res = max(res, dp[i][j])
            idx[A[i]] = i
        return res


if __name__ == '__main__':
    s = Solution()
    A = [20, 1, 15, 3, 10, 5, 8]  # [20,15,10,5]
    # A = [3, 6, 9, 12]
    print(s.longestArithSeqLength(A))
