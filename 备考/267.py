#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = set()
        n = len(s)

        def backtrace(start, temp):
            if ''.join(temp) == ''.join(temp)[::-1] and len(temp) == n:
                ans.add(''.join(temp))
            for i in s:
                backtrace(i + 1, temp + [i])

        backtrace(0, [])

        return ans


if __name__ == '__main__':
    sn = Solution()
    s = 'aabb'
    print(sn.generatePalindromes(s))
