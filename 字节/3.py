#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        tmp = ''
        ans = 0
        for i in range(n):
            if s[i] in tmp:
                tmp = tmp[tmp.index(s[i]) + 1:]
            tmp += s[i]
            ans = max(ans, len(tmp))
        return ans


if __name__ == '__main__':
    sn = Solution()
    s = "abcabcbb"
    print(sn.lengthOfLongestSubstring(s))
