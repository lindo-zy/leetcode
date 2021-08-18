#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = [[bin(i).count('1'), i] for i in arr]
        nums.sort(key=lambda x: (x[0], x[1]))
        return [i[1] for i in nums]


if __name__ == '__main__':
    s = Solution()
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print(s.sortByBits(arr))
