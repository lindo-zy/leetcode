#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):  # i是行数
            for j in range(i):  # j是列数
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # 实现对角线对称

        for m in range(n):
            matrix[m] = matrix[m][::-1]  # 每一行逆序


if __name__ == '__main__':
    sn = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sn.rotate(matrix))
