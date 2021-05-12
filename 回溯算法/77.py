#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrace(start, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(start, n + 1):
                # if i > n - (k - len(tmp)) + 1:
                #     break
                backtrace(i + 1, tmp + [i])

        backtrace(1, [])
        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2

    # n = 3
    # k = 3

    print(s.combine(n, k))
