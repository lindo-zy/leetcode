#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[p[0]], curMaxLen = 1, 1
        for idx in range(1, len(p)):
            if (ord(p[idx]) - ord(p[idx - 1])) % 26 == 1:
                curMaxLen += 1
            else:
                curMaxLen = 1
            dp[p[idx]] = max(dp[p[idx]], curMaxLen)
        print(dp)
        return sum(dp.values())


if __name__ == '__main__':
    s = Solution()
    p = "zab"
    print(s.findSubstringInWraproundString(p))
