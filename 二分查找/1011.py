#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + ((right - left) >> 1)
            cur = 0
            need = 1
            for num in weights:
                cur += num
                if cur > mid:
                    need += 1
                    cur = num
            if need <= D:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    print(s.shipWithinDays(weights, D))
