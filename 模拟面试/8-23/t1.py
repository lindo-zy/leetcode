#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        cm = 1
        cnt = 0
        for i, l in enumerate(light):
            cm = max(cm, l)
            if i + 1 == cm:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    light = [2, 1, 3, 5, 4]
    # light = [3, 2, 4, 1, 5]
    print(s.numTimesAllBlue(light))
