#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum(map(lambda x: x % 2, Counter(s).values()))


if __name__ == '__main__':
    sn = Solution()
    s = "annabelle"
    k = 2
    print(sn.canConstruct(s, k))
