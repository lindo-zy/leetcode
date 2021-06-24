#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ds = defaultdict(int)
        for i in s:
            ds[i] += 1
            if ds[i] == k:
                del ds[i]
        return ''.join(ds.keys())


if __name__ == '__main__':
    sn = Solution()
    s = "pbbcggttciiippooaais"
    k = 2
    # s = "deeedbbcccbdaa"
    # k = 3
    print(sn.removeDuplicates(s, k))
