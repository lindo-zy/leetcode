#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        size = len(A)
        for i in range(size, 1, -1):
            ind = A.index(i)
            A = A[-1:ind:-1] + A[:ind]
            res += [ind + 1, i]
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [3, 2, 4, 1]
    print(s.pancakeSort(arr))
