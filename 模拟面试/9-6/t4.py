#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = 0
        cnt = 0


if __name__ == '__main__':
    s = Solution()
    A = [2, -1, 2]
    K = 3
    print(s.shortestSubarray(A, K))
