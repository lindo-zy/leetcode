#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx + len(part):]
        return s


if __name__ == '__main__':
    sn = Solution()
    # s = "daabcbaabcbc"
    # part = "abc"

    s = "axxxxyyyyb"
    part = "xy"
    print(sn.removeOccurrences(s, part))
