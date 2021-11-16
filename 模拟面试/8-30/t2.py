#!/usr/bin/python3
# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        for i in range(32):
            for j in range(32):
                if x ** i + y ** j <= bound:
                    res.add(x ** i + y ** j)
        return list(res)


if __name__ == '__main__':
    s = Solution()
    x = 2
    y = 3
    bound = 10
    print(s.powerfulIntegers(x, y, bound))
