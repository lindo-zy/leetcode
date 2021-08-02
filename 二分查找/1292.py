#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        def check():
            pass

        # 求解的是正方形边长
        left, right = 0, max(m, n)
        while left < right:
            mid = (left + right) // 2
            if check():
                left = mid + 1
            else:
                right = mid


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    threshold = 6
