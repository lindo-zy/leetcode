#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        res = []

        def dfs(tmp, left, right):
            if left > n or right > left:
                return
            if len(tmp) == n * 2:
                res.append(tmp)
                return
            dfs(tmp + '(', left + 1, right)
            dfs(tmp + ')', left, right + 1)

        dfs('', 0, 0)

        return res


if __name__ == '__main__':
    sn = Solution()
    n = 1
    print(sn.generateParenthesis(n))
