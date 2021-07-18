#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:

        cur = (rungs[0] - 1) // dist
        for i in range(1, len(rungs)):
            temp = rungs[i] - rungs[i - 1]
            if temp > dist:
                cur += (temp - 1) / dist
        return cur


if __name__ == '__main__':
    s = Solution()
    rungs = [3, 4, 6, 7]
    dist = 2
    print(s.addRungs(rungs, dist))
