#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        j = 0
        for i in range(len(s)):
            if s[i] >= g[j]:
                j += 1
            if j == len(g):
                return j
        return j


if __name__ == '__main__':
    sn = Solution()
    g = [1, 2, 3]
    s = [1, 1]
    print(sn.findContentChildren(g, s))
