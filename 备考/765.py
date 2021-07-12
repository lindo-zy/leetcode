#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        res = 0
        for i in range(0, n - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue
            for j in range(i + 1, n):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    row = [0, 2, 1, 3]
    print(s.minSwapsCouples(row))
