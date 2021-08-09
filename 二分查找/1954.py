#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # i, sum = 0, 0
        # while sum < neededApples:
        #     i = i + 2
        #     sum = sum + i * i * 3
        # return i * 4

        def f(i):
            return 2 * i * (i + 1) * (2 * i + 1)

        # f(62996) >= 10 ** 15
        left, right = 1, 63000
        while left < right:
            mid = left + right >> 1
            if f(mid) < neededApples:
                left = mid + 1
            else:
                right = mid
        return 8 * left


if __name__ == '__main__':
    s = Solution()
    neededApples = 13
    print(s.minimumPerimeter(neededApples))
