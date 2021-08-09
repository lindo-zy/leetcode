#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        cnt = 0
        while s > 1:
            if s & 1 == 1:
                s += 1
            elif s & 1 == 0:
                s = s >> 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    sn = Solution()
    s = "1101"
    print(sn.numSteps(s))
