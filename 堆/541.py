#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby


class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted(s)
        res = []
        for i, j in groupby(s):
            res.append(list(j))
        res.sort(key=len)
        ans = ''
        for item in res:
            ans += ''.join(item)
        return ans[::-1]


if __name__ == '__main__':
    sn = Solution()
    # s = "tree"
    # s = "Aabb"
    s = "raaeaedere"
    print(sn.frequencySort(s))
