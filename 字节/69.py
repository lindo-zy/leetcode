#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r ** 2 > x:
            r = (r + x / r) // 2
        return int(r)
