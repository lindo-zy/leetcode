#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            try:
                return haystack.index(needle)
            except Exception:
                return -1

if __name__ == '__main__':
    s = Solution()
    haystack = 'Mississippi'
    needle = 'issip'
    haystack = 'aaaaa'
    needle = 'bba'
    # haystack = 'a'
    # haystack = ''
    # needle = ''
    result = s.strStr(haystack, needle)
    print(result)
