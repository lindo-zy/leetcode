#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return not len(s)


if __name__ == '__main__':
    sn = Solution()
    s = "()[]{}"
    print(sn.isValid(s))
