#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = '.' * n

        def backtrace(path, i, col, z_diag, f_diag):
            if i == n:
                res.append(path)
                return
            for j in range(n):
                if j not in col and i - j not in z_diag and i + j not in f_diag:
                    backtrace(path + [s[:j] + 'Q' + s[j + 1:]], i + 1, col + [j], z_diag | {i - j}, f_diag | {i + j})

        backtrace([], 0, [], set(), set())

        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    print(s.solveNQueens(n))
