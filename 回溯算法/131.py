#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrace(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    backtrace(s[i:], tmp + [s[:i]])

        backtrace(s, [])
        return res


if __name__ == '__main__':
    sn = Solution()
    s = "aab"
    print(sn.partition(s))
