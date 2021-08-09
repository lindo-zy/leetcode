#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row = len(rowSum)
        col = len(colSum)
        matrix = [[0] * col for i in range(row)]
        for i in range(row):
            for j in range(col):
                min_num = min(rowSum[i], colSum[j])
                matrix[i][j] = min_num
                rowSum[i] -= min_num
                colSum[j] -= min_num
                if rowSum[i] == 0:
                    break
        return matrix


if __name__ == '__main__':
    s = Solution()
    rowSum = [3, 8]
    colSum = [4, 7]
    print(s.restoreMatrix(rowSum, colSum))
