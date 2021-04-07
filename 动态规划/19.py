#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m = len(s)
        # n = len(p)
        # dp = [[0 for i in range(m)] for i in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         if s[i] == p[j]:
        #             dp[i][j] = ''
        #         elif s[i] != p[j] and p[j] == '.':
        #             pass
        #         elif s[i] != p[j] and p[j] == '*':
        #             pass
        # return dp[-1][-1] > 0

        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True  # 2.
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True  # 3.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True  # 2.
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = Solution()
    s = 'aab'
    p = 'c*a*b'
    print(s1.isMatch(s, p))
