#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a, k, c = 1, max(piles), len(piles)
        while a < k:
            m = (a + k) // 2
            t = sum((i - 1) // m for i in piles)
            if t + c > h:  # 吃不完
                a = m + 1
            else:
                k = m
        return a


if __name__ == '__main__':
    s = Solution()
    piles = [30, 11, 23, 4, 20]
    H = 6
    print(s.minEatingSpeed(piles, H))
