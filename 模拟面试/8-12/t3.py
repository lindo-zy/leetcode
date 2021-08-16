#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:

        # s替换一个字符，为t的子串
        m = len(s)
        n = len(t)
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    left = 1
                    while i - left >= 0 and j - left >= 0 and s[i - left] == t[j - left]:
                        left += 1
                    right = 1
                    while i + right < m and j + right < n and s[i + right] == t[j + right]:
                        right += 1
                    ans += left * right
        return ans


if __name__ == '__main__':
    sn = Solution()
    s = "aba"
    t = "baba"
    print(sn.countSubstrings(s, t))
