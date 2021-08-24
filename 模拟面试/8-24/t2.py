#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        for i in range(n):
            pass


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.bulbSwitch(n))
