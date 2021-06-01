#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices & 1 == 1:
            return []
        if 2 * cheeseSlices <= tomatoSlices <= 4 * cheeseSlices:
            a = (tomatoSlices - 2 * cheeseSlices) // 2
            b = cheeseSlices - a
            return [a, b]
        return []


if __name__ == '__main__':
    s = Solution()
    tomatoSlices = 16
    cheeseSlices = 7
    print(s.numOfBurgers(tomatoSlices, cheeseSlices))
