#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = '.' * n

        def backtrace(path, row, col, z_diag, f_diag):
            if row == n:
                res.append(path)
                return
            for j in range(n):
                if j not in col and row - j not in z_diag and row + j not in f_diag:
                    backtrace(path + [s[:j] + 'Q' + s[j + 1:]], row + 1, col + [j], z_diag | {row - j},
                              f_diag | {row + j})

        backtrace([], 0, [], set(), set())

        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    print(s.solveNQueens(n))
