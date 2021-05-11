#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        for right in range(len(s)):
            if s[right] not in s[left:right]:
                maxLen = max(maxLen, right - left + 1)
                continue
            left = left + s[left:right].index(s[right]) + 1
        return maxLen


if __name__ == '__main__':
    sn = Solution()
    s = 'pwwkew'  # 3
    print(sn.lengthOfLongestSubstring(s))
