#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        left = defaultdict(int)
        right = collections.Counter(s)

        for i in s:
            left[i] += 1
            right[i] -= 1
            if len(left) == len(list(filter(lambda k: k[1] > 0, right.items()))):
                res += 1

        return res


if __name__ == '__main__':
    sn = Solution()
    s = "aacaba"
    print(sn.numSplits(s))
