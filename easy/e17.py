#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (x / r + r) // 2
        return int(r)


if __name__ == '__main__':
    s = Solution()
    x = 8
    print(s.mySqrt(x))
