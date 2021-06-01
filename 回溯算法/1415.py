#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        chars = ['a', 'b', 'c']

        def backtrace(tmp, s):
            if len(s) == n:
                ans.append(s)
                return
            for c in set(chars) - tmp:
                backtrace({c}, s + c)

        backtrace(set(), '')
        ans.sort()
        if len(ans) < k:
            return ""
        return ans[k - 1]


if __name__ == '__main__':
    s = Solution()
    n = 1
    k = 4
    print(s.getHappyString(n, k))
