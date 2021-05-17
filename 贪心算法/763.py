#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ds = {}
        for index, c in enumerate(s):
            ds[c] = index
        left = 0
        right = 0
        res = []
        for i in range(len(s)):
            right = max(right, ds[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res


if __name__ == '__main__':
    sn = Solution()
    s = "ababcbacadefegdehijhklij"
    print(sn.partitionLabels(s))
