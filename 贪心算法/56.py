#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(s.merge(intervals))
