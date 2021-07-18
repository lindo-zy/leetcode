#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        ans = 0

        return ans


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    print(s.smallestCommonElement(mat))
