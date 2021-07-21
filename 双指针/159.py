#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        res = float("-inf")
        for right in range(len(s)):
            while len(set(s[left:right + 1])) > 2:
                left += 1
            res = max(res, right - left + 1)
        return res


if __name__ == '__main__':
    sn = Solution()
    s = "ccaabbb"
    print(sn.lengthOfLongestSubstringTwoDistinct(s))
