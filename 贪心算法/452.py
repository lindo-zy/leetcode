#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        cnt = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                cnt += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])
        return cnt


if __name__ == '__main__':
    s = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]  # 2
    print(s.findMinArrowShots(points))
