#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ""


if __name__ == '__main__':
    sn = Solution()
    s = '([)]'
    s = '{[]}'
    # s = '(]'
    # s = '[])'
    result = sn.isValid(s)
    print(result)
