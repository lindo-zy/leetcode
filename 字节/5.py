#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        start = 0

        # 中心扩散法
        def check(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(n):
            len1 = check(i, i)
            len2 = check(i, i + 1)
            cur_len = max(len1, len2)
            if cur_len > max_len:
                max_len = cur_len
                start = i - (cur_len - 1) // 2

        return s[start:start + max_len]
