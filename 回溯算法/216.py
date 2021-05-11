#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrace(start, tmp):
            if sum(tmp) == n and len(tmp) == k:
                res.append(tmp[:])
                return
            if sum(tmp) > n or len(tmp) > k:
                return
            for i in range(start, 10):
                backtrace(i + 1, tmp + [i])

        backtrace(1, [])
        return res


if __name__ == '__main__':
    s = Solution()
    # k = 3
    # n = 7

    k = 3
    n = 9
    print(s.combinationSum3(k, n))
