#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0

        if '0' not in s:
            return True

        for num, item in groupby(s):
            cnt += 1
        if cnt != 2:
            return False
        return True


if __name__ == '__main__':
    sn = Solution()
    s = "11"
    print(sn.checkOnesSegment(s))
