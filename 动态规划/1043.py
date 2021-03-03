#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for i in range(1, len(arr) + 1):
            localMax = 0
            for x in range(1, min(k, i) + 1):  # min(k,i)保证长度不超过K
                localMax = max(localMax, arr[i - x])
                # dp[i - x] + x * localMax表示在k长度中，不分的数和分的数之和
                dp[i] = max(dp[i], dp[i - x] + x * localMax)
        return dp[-1]


if __name__ == '__main__':
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    sn = Solution()
    print(sn.maxSumAfterPartitioning(arr, k))
